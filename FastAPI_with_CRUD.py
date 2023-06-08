from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(Item):
    name: Optional[int]= None
    price: Optional[float]= None
    brand: Optional[str]= None

app = FastAPI()

inventory = {}


@app.get('/')
async def root():
    return {"message: Hello World"}


@app.get('/get_item/{item_id}')
def get_item(item_id: int):
    if item_id in inventory:
        return inventory[item_id]
    return {'Error: ': "item not in inventory"}


@app.post('/create_item/{item_id}')
async def create(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error: ": "Item already in inventory"}
    inventory[item_id] = item
    return inventory[item_id]

@app.put('/update_item/{item_id}')
async def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        return {"Error: ": "Item not in inventory"}
    if item.name is not None:
        inventory[item_id].name = item.name
    if item.price is not None:
        inventory[item_id].price = item.price
    if item.brand is not None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete('/delete_item/{item_id}')
def delete_item(item_id: int):
    if item_id not in inventory:
        return {"Error: ": "Item not in inventory"}
    del inventory[item_id]
    return {"Item has been deleted"}


uvicorn.run(app)
