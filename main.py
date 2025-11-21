from fastapi import FastAPI


app=FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.get("/about")
def about_page():
    return {"about myself": "Backend Developer"}

@app.get("/item/{item_id}")
def item_page(item_id: int):
    return {"raqam": f"siz {item_id} raqamini kiritingiz: "}

@app.get("/users/{user_id}/posts/{post_id}")
def read_user_post(user_id: int,post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
@app.get("/student/{ism}")
def student(ism:str):
    return{"student": f"{ism} Backend dasturchi"}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }
    
