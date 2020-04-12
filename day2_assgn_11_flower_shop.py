#OOPR-Assgn-11
#Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
        
    def set_flower_name(self, flower_name):
        self.__flower_name=flower_name.lower()
    def get_flower_name(self):
        return self.__flower_name
    
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
    def get_price_per_kg(self):
        return self.__price_per_kg
    
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
    def get_stock_available(self):
        return self.__stock_available
    
    def validate_flower(self):
        if self.__flower_name=="orchid" or self.__flower_name=="rose" or self.__flower_name=="jasmine":
            return True
        else:
            return False
    
    def validate_stock(self,required_quantity):
        if required_quantity <= self.__stock_available:
            return True
        else:
            return False
    
    def sell_flower(self, required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available -= required_quantity
    
    def check_level(self):
        if self.__flower_name=="orchid" and self.__stock_available < 15:
            return True
        elif self.__flower_name=="rose" and self.__stock_available < 25:
            return True
        elif self.__flower_name=="jasmine" and self.__stock_available < 40:
            return True
        else:
            return False
            
f1=Flower()
f1.set_flower_name("Jasmine")
f1.set_stock_available(40)
f1.set_price_per_kg(1000)
f1.sell_flower(20)