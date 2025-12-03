from fastapi import APIRouter,status,Header
from fastapi.responses import Response,HTMLResponse,PlainTextResponse
from typing import Optional,List

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch','camera','phone']

@router.get("/all",status_code=status.HTTP_200_OK)
def get_products():
    data = " ".join(products)
    response = Response(content=data,media_type="text/plain")
    response.set_cookie(key="test_cookie",value="test_cookie_value")
    return response

@router.get("/withHeader")
def get_products(
    response: Response,
    custom_header: Optional[List[str]] = Header(None)):
    if custom_header:
        response.headers['X-Custom-Response-Header'] = ", ".join(custom_header)
    return products



@router.get("/{id}",status_code=status.HTTP_200_OK,responses={
    200:{"content":{
        "text/html":{
            "<div> Product </div>"
        },
        "description" : "Returns the HTML for an object."

    }},404:{
        "content" :{
            "text/plain" :{
                "Product Not Available"
            },
            "description" : "Returns the Product"
        }
    }
})
def get_products(id:int):
    if id >len(product):
        out = "Product Not Available"
        return PlainTextResponse(content=out,media_type="text/plain")
    else:
        product = products[id]
        out = f'''  
        <head>
        <style>
 
        .product {{
        width: 500px;
        height: 30px;
        border: 2px inset green;
        background-color: lightblue;
        text-align : center;
        }}

        </style>
        </head>

        <div class = "product">{product}</div>

        '''

        return HTMLResponse(content=out,media_type="text/html")
    


