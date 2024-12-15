class name1:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. I am {self.age} years old.")

class name2:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am {self.name}. I am {self.age} years old.")

firstname = name1("Anjali" , 15) 
secondname = name2("Cat" , 3) 

for names in (firstname,secondname):
    names.info()


class Computer:

    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 2000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
