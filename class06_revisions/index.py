# pip install requests
import requests

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




###### Dictionary
student_info = {
    'roll_number': 183927,
    'name': 'Ali Ahmed',
    'courses': ['Docker', 'FastAPI','OpenAI Agents'],
    'assignments': { 
        'assignOne': 'completed',
        'assignTwo': 'InProgress'
    }
}
print(student_info)
print(student_info['courses'][2])
print(student_info['courses'][-1])
print(student_info['assignments']['assignTwo'])


for abcd in student_info.values():
    print(abcd)

for keys, values in student_info.items():
    print(keys, values)

for i in range(100, 120):
    print(i)


try:
  req = requests.get("https://jsonplaceholder.typicode.com/posts")
  print(req.json())
except Exception as e:
  print(e)
  print("Error agya bhai saab")
else:
  print("Yahha tak pohnch gya") 



try:
    url = requests.get('https://jsonplaceholder.typicode.com/posts')
    res = url.json()
    print(res)
except Exception as e:
    print(e)
finally:
    print("Request Ended")


