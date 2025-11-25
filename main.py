from fastapi import FastAPI,status,Response
from enum import Enum
from typing import Optional


app = FastAPI()

class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"

@app.get("/")
def root_folder():
    return {
        "message" : "Hey!"
    }

@app.get("/blogs/all",tags=['blog'],summary='Reterive all blogs',description='This api call simulates',response_description='The list of available blogs')
def get_all_blogs(page:int = 2,page_size:Optional[int] = None):
    return {
        "message" : f"All {page} are {page_size}"
    }


@app.get("/blog/type/{btype}",tags=['blog'])
def get_blog_type(type: BlogType):
    return {
        "message" : f"Blog Type : {type}"
    }

@app.get("/blog/{id}",status_code=status.HTTP_200_OK,tags=['blog'])
def get_blog(id:int,response:Response):
    if id> 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found!!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': 'Default!!'}

@app.get("/blog/{id}/comments/{comment_id}",tags=['blog','comment'])
def get_blog_comment(id:int,comment_id:int,valid:bool= True, username: Optional[str]= None):
    return {
        'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'
    }