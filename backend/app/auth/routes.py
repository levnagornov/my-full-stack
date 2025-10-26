from fastapi import APIRouter, Response, Depends, Cookie
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional

from app.auth import service, schemas
from app.core.database import get_session


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=dict)
async def register(data: schemas.RegisterRequest, session: AsyncSession = Depends(get_session)):
    return await service.register_user(data, session)


@router.post("/login", response_model=schemas.TokenResponse)
async def login(data: schemas.LoginRequest, response: Response, session: AsyncSession = Depends(get_session)):
    return await service.login_user(data, response, session)


@router.post("/refresh", response_model=schemas.TokenResponse)
async def refresh(response: Response, refresh_token: Optional[str] = Cookie(None)):
    return await service.refresh_tokens(response, refresh_token)


@router.post("/logout")
async def logout(response: Response, refresh_token: Optional[str] = Cookie(None)):
    return await service.logout_user(response, refresh_token)
