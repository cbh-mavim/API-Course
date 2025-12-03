from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import JSONResponse,PlainTextResponse
from app.routers import blog_get,blog_post,users,article,product
from app.models import models
from app.db.database import engine
from exceptions import StoryException
from fastapi.middleware.cors import CORSMiddleware
from app.auth import authentication


app = FastAPI()
app.include_router(authentication.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(users.router)
app.include_router(article.router)
app.include_router(product.router)




@app.get("/")
def root_folder():
    return {
        "message" : "Hey!"
    }


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc:StoryException ):
    return JSONResponse(
        status_code= 418, #Exception Status Code
        content= {
            "detail" : exc.name
        }
    )

@app.exception_handler(HTTPException)
def custom_hanler(request:Request,exc: StoryException):
    return PlainTextResponse(str(exc),status_code=400)

models.Base.metadata.create_all(engine)

origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)