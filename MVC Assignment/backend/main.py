from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model, controller
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = model.ItemModel()
controller = controller.ItemController(model)

@app.get("/api/items")
def get_items():
    items = controller.get_items()
    return items
