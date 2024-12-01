lst = ['Badminton', 'Cricket', 'Tennis']

print("Length of list:", len(lst))
print("First Element:", lst[0])
print("Last Element:", lst[-1])

lst.append('Badminton')
print("Updated List :", lst)

lst.remove('cricketl')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List:", lst)

lst.reverse()
print("Reversed List:", lst)

print("Multiplication on list :", lst*2)

lst = lst[:4]
print("Sliced list :" , lst)

lst.clear()
print("Updated list :" , lst)




# empty dictionary
my_dict ={}

#dictionary with integer keys
my_dict = {1: 'apple',2: 'ball'}

#dictionary with mixed keys
my_dict = {'name': 'Anjali', 'age': 15}

#Output: Jack
print(my_dict['name'])
print(my_dict.get['age'])

# remove all the elements
my_dict.clear()
print(my_dict)
