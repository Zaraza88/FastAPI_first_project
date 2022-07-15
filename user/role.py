from typing import List

from fastapi import Depends, HTTPException, status

from user.schemas import BaseUserSchema
from auth.depends import get_current_user
from user.user_db import user_crud


def admin_permission(user: BaseUserSchema = Depends(get_current_user)):
    if not user_crud.is_admin(user):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Операция недоступна")


# def staff_permission(user: BaseUserSchema = Depends(get_current_user)):
#     if not user_crud.is_staff(user):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Операция недоступна")


# def manager_permission(user: BaseUserSchema = Depends(get_current_user)):
#     if not user_crud.is_manager(user):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Операция недоступна")


# def active_permission(user: BaseUserSchema = Depends(get_current_user)):
#     if not user_crud.is_active(user):
#         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Операция недоступна")
