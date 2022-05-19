import json
import Item

class ItemStore:
    items = [Item.Item]
    
    def addItem(self, name, quantity):
        item = Item.Item(name, quantity)
        
        self.items.append(item)
        
        item.id = self.items.index(item)
        
        return item
    
    def removeItem(self, index):
        self.items.remove(self.items[index])
        
    def toJSON(self):
        return json.dumps(self.items, 
                          default=lambda 
                          o: o.__doc__ ,   
                          sort_keys=True, 
                          indent=4)