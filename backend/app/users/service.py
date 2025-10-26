from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.auth import models


async def get_user_by_username(username: str, session: AsyncSession):
    q = await session.execute(select(models.User).where(models.User.username == username))
    return q.scalar_one_or_none()
