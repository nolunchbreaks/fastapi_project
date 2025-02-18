from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Welcome to my FastAPI app!"}
# In-memory database
items = {}

# Item model
class Item(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


# Create an item
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in items:
        raise HTTPException(status_code=400, detail="Item already exists")
    items[item_id] = item
    return {"message": "Item created", "item": item}


# Read all items
@app.get("/items")
def read_items():
    return items


# Read a specific item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


# Update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    items[item_id] = item
    return {"message": "Item updated", "item": item}


# Delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"message": "Item deleted"}
