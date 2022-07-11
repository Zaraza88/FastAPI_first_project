from fastapi import FastAPI

from routers import blog, user
from core.database import engine
from blog import models


app = FastAPI()


app.include_router(user.router)
app.include_router(blog.router)


models.Base.metadata.create_all(engine)
