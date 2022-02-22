import csv
from logging import raiseExceptions

class Item:
    pay_rate = 0.8 #pay rate after 20 parcent discunt
    all = []
    def __init__(self,name: str, price: float, quantity=0):

        assert price >= 0, f"Price {price} is not greater then zero"
        assert quantity >= 0, f"quentity {quantity} is not greater then zero"
        #assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # actions to exiscute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price
    
    def pay_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value   

    @property
    def name(self):
        return self.__name
    
    #setter method
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raiseExceptions("The name is too long")
        self.__name = value    

    def calculate_total_price(self):
       return self.quantity * self.__price





    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity= int(item.get('quantity')),
            )        
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False            

    def __repr__(self):
         return f"{self.__class__.__name__}({self.name}, {self.price}, {self.quantity})" 
    

    def conncet(self, smtp_server):
        pass 

    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.name} and {self.quantity} times
        Regards, Azharul        
        """

    def __send(self):
        pass

    def send_email(self):
        # self.__conncet('')
        self.__prepare_body()
        self.__send()   