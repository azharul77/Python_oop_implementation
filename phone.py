from item import Item

class Phone(Item):
    
    def __init__(self,name: str, price: float, quantity=0,broken_phone=0):
        # call super function to have access to all attributes/ methos
        super().__init__(
             name, price, quantity
        )

        assert broken_phone >=0, f"Broken Phones{broken_phone} is not greater or equal" 

      
        self.broken_phone = broken_phone


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
phone2 = Phone("jscPhonev20", 700, 5, 1)

print(Item.all)
print(Phone.all)

