from fastapi import APIRouter,status,Response
from typing import Optional
from models import basemodel

router = APIRouter(
    prefix= '/blog',
    tags=['blog']
)

@router.get("/all",summary='Reterive all blogs',description='This api call simulates',response_description='The list of available blogs')
def get_all_blogs(page:int = 2,page_size:Optional[int] = None):
    return {
        "message" : f"All {page} are {page_size}"
    }

@router.get("/type/{btype}")
def get_blog_type(type: basemodel.BlogType):
    return {
        "message" : f"Blog Type : {type}"
    }

@router.get("/{id}",status_code=status.HTTP_200_OK)
def get_blog(id:int,response:Response):
    if id> 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error' : f'Blog {id} not found!!'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': 'Default!!'}

@router.get("/{id}/comments/{comment_id}",tags=['comment'])
def get_blog_comment(id:int,comment_id:int,valid:bool= True, username: Optional[str]= None):
    return {
        'message' : f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'
    }