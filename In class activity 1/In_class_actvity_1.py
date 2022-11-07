import os,time,string,random


class vending_machine:
    def __init__(self) -> None:
        pass
class hot_beverage:
    def __init__(self, name, addon="", size=""):
        self.name = name
        self.addon = addon
        self.size = size
    def change_addon(self,addon):
        self.addon = addon
    def change_size(self,size):
        self.size = size
    def __str__(self) -> str:
        return "You want "+self.size +" "+ self.name +" with " +self.addon
class coffee(hot_beverage):
    pass
class tea(hot_beverage):
    pass
class condiments:
    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
    def __str__(self):
        return "You want "+self.name+ " " + self.amount
class sugar(condiments):
    pass
    def __init__(self,name,amount):
       super().__init__(name,amount)
       
class milk(condiments):
    pass
    def __init__(self,name,amount):
       super().__init__(name,amount)

class Espresso(coffee):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)

class Americano(coffee):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)

class Latte_Macchiato(coffee):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)
        
class blacktea(tea):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)
class greentea(tea):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)
class yellowtea(tea):
    def __init__(self,name,addon,size):
        super().__init__(name, addon, size)
 

def clear_screen(sec):
    print("Screen cleaning in " + str(sec) +" seconds. ")
    time.sleep(sec)
    # clean the screen. 
    os.system('cls' if os.name == 'nt' else 'clear')
# def user_interface()

def askcondiment():
    addsugar = int(input("would you like some sugar? (0-3)"))
    sugars = sugar("sugar",addsugar)
    addmilk = int(input("would you like some milk ?(0-3)"))
    milks = milk("milk",addmilk)
    return sugars,milks

def display(product,condiment1,condiment2):
    print(product)
    print(condiment1)
    print(condiment2)
    return
def detail(product):
    size = input("Would you like large, mid, small?\n")
    product.change_size(size)
    addon = input("What addon would you like?\n")
    product.change_addon(addon)
    condiment1,condiment2 = askcondiment()
    display(product,condiment1,condiment2)

def main():
    while 1:
        item = input("What would you like, coffee or tea?\n")
        if item == "coffee":
            item = input("What kind of coffee would you like, Espresso, Americano, or Latte Macchiato? \n")
            if item == "Espresso":
                product = Espresso(item,"","")
                detail(product)
            elif item == "Americano":
                product = Americano(item,"","")
                detail(product)
            elif item == "Latte Macchiato":
                product = Latte_Macchiato(item,"","")
                detail(product)
        
        elif item == "tea":
            item = input("What kind of tea would you like,  black, green, or yellow? \n")
            if item == "black":
                product = blacktea("Black Tea","","")
                detail(product)
            elif item == "green":
                product = Americano("Green Tea","","")
                detail(product)
            elif item == "yellow":
                product = Latte_Macchiato("Yellow Tea","","")
                detail(product)
        
if __name__ == "__main__":
    main()
    