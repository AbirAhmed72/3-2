from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    description: str

class ItemModel:
    def get_items(self):
        return [
            {"name": "Oppo", "description": "Oppo good 1"},
            {"name": "Vivo", "description": "Vivo good 2"}
        ]

class ItemController:
    def __init__(self, model):
        self.model = model

    def get_items(self):
        return self.model.get_items()

model = ItemModel()
controller = ItemController(model)

@app.get("/api/items")
def get_items():
    items = controller.get_items()
    return items
