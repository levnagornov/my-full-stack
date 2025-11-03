from fastapi import HTTPException, Response, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Optional
import logging
from app.auth import schemas, models
from app.core import security

logger = logging.getLogger(__name__)

async def register_user(data: schemas.RegisterRequest, session: AsyncSession):
    logger.info(f"Register request for {data.username}")
    q = await session.execute(select(models.User).where(models.User.username == data.username))
    user = q.scalar_one_or_none()
    if user:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = models.User(
        username=data.username,
        password_hash=security.hash_password(data.password)
    )
    session.add(user)
    await session.commit()
    logger.info(f"New user has been registered: {data.username}")
    return {"detail": "User created"}


async def authenticate_user(username: str, password: str, session: AsyncSession):
    q = await session.execute(select(models.User).where(models.User.username == username))
    user = q.scalar_one_or_none()
    if not user or not security.verify_password(password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user


async def login_user(data: schemas.LoginRequest, response: Response, session: AsyncSession):
    logger.info(f"Login request for username={data.username} password={data.password}")
    user = await authenticate_user(data.username, data.password, session)
    access = security.create_access_token(user.username)
    refresh, jti = security.create_refresh_token(user.username)
    await security.store_refresh_token(jti, user.username)

    response.set_cookie(
        key="refresh_token",
        value=refresh,
        httponly=True,
        secure=True,
        samesite="lax",
        path="/",
        max_age=security.settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400
    )
    return schemas.TokenResponse(access_token=access)


async def refresh_tokens(response: Response, refresh_token: Optional[str] = Cookie(None)):
    if not refresh_token:
        raise HTTPException(status_code=401, detail="No refresh token")

    payload = security.decode_token(refresh_token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    jti = payload.get("jti")
    username = payload.get("sub")

    if not await security.is_refresh_valid(jti, username):
        raise HTTPException(
            status_code=401, detail="Refresh token revoked or expired")

    await security.revoke_refresh_token(jti)

    new_access = security.create_access_token(username)
    new_refresh, new_jti = security.create_refresh_token(username)
    await security.store_refresh_token(new_jti, username)

    response.set_cookie(
        key="refresh_token",
        value=new_refresh,
        httponly=True,
        secure=True,
        samesite="lax",
        path="/",
        max_age=security.settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400
    )

    return schemas.TokenResponse(access_token=new_access)


async def logout_user(response: Response, refresh_token: Optional[str] = Cookie(None)):
    if refresh_token:
        payload = security.decode_token(refresh_token)
        if payload and payload.get("jti"):
            await security.revoke_refresh_token(payload["jti"])
    response.delete_cookie("refresh_token", path="/")
    return {"detail": "Logged out"}
