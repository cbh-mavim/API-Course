from fastapi import FastAPI
from app.routers import blog_get,blog_post,users,article
from app.models import models
from app.db.database import engine

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(users.router)
app.include_router(article.router)


@app.get("/")
def root_folder():
    return {
        "message" : "Hey!"
    }

models.Base.metadata.create_all(engine)
