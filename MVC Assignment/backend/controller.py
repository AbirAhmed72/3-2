class ItemController:
    def __init__(self, model):
        self.model = model

    def get_items(self):
        return self.model.get_items()