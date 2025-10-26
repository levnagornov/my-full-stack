from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from app.core import security


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_username(token: str = Depends(oauth2_scheme)) -> str:
    payload = security.decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload["sub"]
