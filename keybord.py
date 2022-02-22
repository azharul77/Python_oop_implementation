from item import Item

class Keybord(Item):
    
    def __init__(self,name: str, price: float, quantity=0):
        # call super function to have access to all attributes/ methos
        super().__init__(
             name, price, quantity
        )

      