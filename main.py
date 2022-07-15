from fastapi import FastAPI

from routers import blog, user, auth
from core.database import engine
from blog import models


app = FastAPI()


app.include_router(user.router)
app.include_router(blog.router)
app.include_router(auth.router)


models.Base.metadata.create_all(engine)
