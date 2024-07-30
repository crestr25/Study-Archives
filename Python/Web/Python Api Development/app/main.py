from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel


app = FastAPI()

my_posts = []
counter = 0

# Pydantic Models
class Post(BaseModel):
    # model.dict() turns the pydantic model to a dictionary
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

# @app.get("/posts")
# @app.get("/posts/{id}")
# @app.post("/posts")
# @app.put("/posts/{id}")
# @app.delete("/posts/{id}")

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return {"data": post}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()

    global counter
    post_dict["id"] = counter
    counter += 1

    my_posts.append(post_dict)
    return {"data": post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            my_posts.pop(i)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")

@app.put("/posts/{id}")
def modify_post(id: int, post: Post):
    new_post = post.model_dump()
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            my_posts.pop(i)
            new_post["id"] = id
            my_posts.insert(i, new_post)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")


