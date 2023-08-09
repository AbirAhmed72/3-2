from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

class ItemModel:
    def get_items(self):
        return [
            {"name": "Oppo", "description": "Oppo good 1"},
            {"name": "Vivo", "description": "Vivo good 2"}
        ]