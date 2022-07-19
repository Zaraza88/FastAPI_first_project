# import os
# import sys
# from pydantic import EmailStr
# from sqlalchemy.orm import Session
# from fastapi import Depends



# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# from user.user_db import user_crud
# from user.schemas import UserCreateSchemas
# from core.database import get_db
# from auth.depends import get_by_email


# def main(db: Session):
#     """ Создание супер юзера
#     """

#     print("Create superuser")
#     name = input("Username: ")
#     email = input("Email: ")
#     password = input("Password: ")
#     password_two = ('Repeat password: ')

#     super_user = get_by_email(db, email)
#     if not super_user:
#         user = UserCreateSchemas(
#             username=name,
#             email=email,
#             password=password,
#             password2=password_two
#         )
#         user_crud.create_superuser(user, db)
#         print("Success")
#     else:
#         print("Error, user existing")


# if __name__ == '__main__':
#     main(Session = Depends(get_db))