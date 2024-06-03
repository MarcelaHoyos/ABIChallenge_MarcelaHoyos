from fastapi import FastAPI

class Item:
    def __init__(self, item_id: int, description: str):
        self.item_id = item_id
        self.description = description

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint returning a simple welcome message.
    """
    return {"message": "Hello, world!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Punto final para recuperar un elemento por su ID y un parámetro de consulta opcional.

    :param item_id: ID of the item
    :param q: Optional query string
    :return: JSON with the item ID and query string
    """
    item = Item(item_id, q)
    return {"item_id": item.item_id, "description": item.description}
