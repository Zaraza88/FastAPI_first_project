from dotenv import load_dotenv

import os


load_dotenv()

SQL_DATABASE = os.getenv('SQL_DATABASE')


#token
SECRET_KEY = 'fba012a2a0c9c3d884fdf15843f2aa438bac1b5e8527875ecd7187e3ce494158'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30