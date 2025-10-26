from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from uuid import uuid4
import redis.asyncio as aioredis

from app.core.config import settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

redis_client = aioredis.from_url(
    f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", decode_responses=True
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(username: str) -> str:
    expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": username, "exp": expire}
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def create_refresh_token(username: str) -> tuple[str, str]:
    token_id = str(uuid4())
    expire = datetime.now() + timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode = {"sub": username, "jti": token_id, "exp": expire}
    token = jwt.encode(to_encode, settings.SECRET_KEY,
                       algorithm=settings.ALGORITHM)
    return token, token_id


def decode_token(token: str):
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None


async def store_refresh_token(jti: str, username: str):
    await redis_client.setex(
        f"refresh:{jti}",
        settings.REFRESH_TOKEN_EXPIRE_DAYS * 86400,
        username
    )


async def revoke_refresh_token(jti: str):
    await redis_client.delete(f"refresh:{jti}")


async def is_refresh_valid(jti: str, username: str) -> bool:
    stored = await redis_client.get(f"refresh:{jti}")
    return stored == username
