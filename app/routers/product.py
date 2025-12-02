from fastapi import APIRouter,status
from fastapi.responses import Response,HTMLResponse,PlainTextResponse

router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ['watch','camera','phone']

@router.get("/all",status_code=status.HTTP_200_OK)
def get_products():
    data = " ".join(products)
    return Response(content=data,media_type="text/plain")

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