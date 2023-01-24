from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ml import obtain_image

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    # This endpoint expects a item_id as a path param
    return {"item_id": item_id}


class Item(BaseModel):
    # Pydantic uses type annotations to verify the data being sent
    name: str
    price: float
    tags: list[str] = []


@app.post("/items/")
def create_item(item: Item):
    return item


@app.get("/generate")
def generate_image(prompt: str):
    # this one receives a parameter that is not in the path, so it defaults to a query
    # param
    image = obtain_image(prompt, num_inference_steps=10, seed=1024)
    image.save("image.png")
    return FileResponse("image.png")
