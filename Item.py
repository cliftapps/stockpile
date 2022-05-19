import json

class Item:
    id: int
    name: str
    quantity: int
    
    def __init__(self, name, quantity):
        self.id = id
        self.name = name
        self.quantity = quantity
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)