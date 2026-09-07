from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.database import get_db
from app.core.security import decode_token
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/login"
)


def get_current_user(
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
) -> User:
    """Dependency: decodes JWT token and retrieves authenticated User."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate authentication credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception

    user_id: Optional[str] = payload.get("sub")
    if user_id is None:
        raise credentials_exception

    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Inactive user account")

    return user


def get_current_agronomist(
    current_user: User = Depends(get_current_user),
) -> User:
    """Dependency: enforces agronomist, researcher, or admin privileges."""
    if current_user.role not in ["agronomist", "researcher", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="The requested action requires agronomist or researcher credentials",
        )
    return current_user


def get_current_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    """Dependency: enforces administrator privileges."""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator privileges required",
        )
    return current_user
