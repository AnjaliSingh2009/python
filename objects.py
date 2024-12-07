class student:
    grade = 9
    print("Hi I'm student of grade" , grade)
    ob = student()

class Parrot:
         #class attribute
         species = "bird"

         # instance attribute
         def __init__(self,name,age):
              self.name = name
              self.age = age

# instantiate the parrot class
blu = Parrot("Blu" , 10)
woo = Parrot("woo" , 15)

#access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is a {}".format(woo.species))

# access the intance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))


class Parrot:
      # instance attribute
         def __init__(self,name,age):
              self.name = name
              self.age = age

              #instance method
        
         def sing(self,song):
               return f"{self.name} sings{song}"

         def dance(self):
               return f"{self.name} is now dancing"

#instantiate the object
blu = Parrot("Blu",15)

print(blu.sing("'Happy"))
print(blu.dance)
                    
