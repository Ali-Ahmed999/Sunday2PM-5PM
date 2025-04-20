# List 
months: list = ['January' , 'Febuary', 'March', 'April', 'May', 'June', 'July', 'Aug']
months[0] = 'Dec'
print(months)
print(months[0:3])
# Slicing List 
print(months[3:6])

print(months[3:])

# # Negative Indexing
print(months[-3:-1])




##### Tuples
numbers: tuple = (12,93,-21,15,27,57)
# numbers[0] = 813 // Error

print(numbers[-4: -1])
print(numbers[0:3])

# Tuples
teachers_names: tuple[str] = ('Ali Jawwad', 'Haseeb', 'Ahmed')
print(teachers_names)
print(type(teachers_names))

# tuple to list conversion
tuple_to_list = list(teachers_names)
print(tuple_to_list)
print(type(tuple_to_list))

# Adding elem to list
print(tuple_to_list.append('Sir Ameen'))
print(tuple_to_list)

# Converting the list back to tuple
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)
print(type(list_to_tuple))