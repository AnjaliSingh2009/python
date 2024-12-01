# tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

# tuple having mixed datatypes
my_tuple = (1,"hello",3.5)
print(my_tuple)

# nested tuple 
my_tuple = (1,"mouse",[8,4,6]3)
print(my_tuple)

# Accessing tuple elements using indexing
my_tuple = ('a' , 'b' , 'c')
print(my_tuple[0])
print(my_tuple[5])

# nested tuple 
my_tuple = (1,"mouse",[8,4,6]3)

# nested tuple
print(n_tuple[0][3])
print(n_tuple[2][0])


#Slicing
print("Sliced :" , my_tuple[1:4])

# Iterating through tuple
for letter in (my_tuple):
    print("Hello" , letter)



my_set = {1,2,3,4,5}
print("Set :" , my_set)

my_set.add(5)
print("Updated Set:" , my_set)

set1 = my_set
set2 = {2,4,4,6}

print("\nset 1" , set1)
print("Set 2" , set 2)
print("Difference")
print(set1.difference(set2))
print("Symmetric Difference")
print(set1.symmetric(set2))

setx = {"green" , "blue"}
sety = {"red" , "blue"}
print("Original set element")
print(setx)
print(sety)
print("\nIntersection of two said sets :")
setz = setx.intersection(sety)
print(setz)
