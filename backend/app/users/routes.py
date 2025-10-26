from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from app.users.service import get_user_by_username
from app.auth.dependencies import get_current_username
from app.core.database import get_session


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me")
async def me(username: str = Depends(get_current_username), session: AsyncSession = Depends(get_session)) -> dict[str, Any]:
    user = await get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404)
    return {"id": user.id, "username": user.username}
