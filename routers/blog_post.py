from fastapi import APIRouter,Query,Body,Path
from models import basemodel
from typing import Optional,List

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.post("/new/{id}")
def create_blog(blog: basemodel.BlogModel,id:int,version:int=1):
    return {
        'data': blog,
        'id' : id,
        'version': version
    }

@router.post("/new/{id}/comment")
def create_comment(blog:basemodel.BlogModel,id:int,comment_title: int = Query(None,title="Id for the comment",description="A comment id",alias="commentId",deprecated=True),
                   v:Optional[List[str]] = Query(None),
                   comment_id: int = Path(None,gt =2),content:str = Body(Ellipsis,regex='^[a-z]\s')):
    return {
        'data': blog,
        'id':id,
        'version':comment_id,
        'content': content,
        'version':v
    }