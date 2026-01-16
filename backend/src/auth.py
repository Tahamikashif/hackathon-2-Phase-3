from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
import jwt
from typing import Optional
from sqlmodel import Session, select
from .database import get_session
from .models.user import User


security = HTTPBearer()


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    """
    Verify the JWT token and return the user ID.
    
    Args:
        credentials: HTTP Authorization credentials containing the token
        
    Returns:
        User ID if token is valid
        
    Raises:
        HTTPException: If token is invalid or user doesn't exist
    """
    token = credentials.credentials
    
    try:
        # Decode the JWT token
        payload = jwt.decode(
            token, 
            os.getenv("BETTER_AUTH_SECRET"), 
            algorithms=["HS256"]
        )
        
        user_id: str = payload.get("userId")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        
        return user_id
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )


def get_current_user(
    token: str = Depends(verify_token),
    session: Session = Depends(get_session)
) -> User:
    """
    Get the current user based on the token.
    
    Args:
        token: User ID from the verified token
        session: Database session
        
    Returns:
        User object if exists
        
    Raises:
        HTTPException: If user doesn't exist
    """
    user = session.exec(select(User).where(User.id == token)).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return user