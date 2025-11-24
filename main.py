from fastapi import FastAPI 


app = FastAPI()


@app.get("/")
def root_folder():
    return {
        "message" : "Hey!"
    }