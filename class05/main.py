name: str = 'Ali'
phonenumber: int = 29482093483
age: float = 12.43
colors: list = ['red' , 'green']
colors2: list[str] = ['red' , 'green', 89]


fruits_name: set = {'apple' , 'apple', 'orange' , 'grapes'}

print(fruits_name) #
# print(fruits_name[0]) # Error


# Union
electronic_cust: set = {'ali' , 'ahmed' , 'nabeel'}
garments_cust: set = {'zargham', 'ahmed' , 'sami'} 
merge = electronic_cust.union(garments_cust)
print(merge)


wow_react:set = {'usman' , 'ali' , 'hussain'}
laugh_react: set = {'daniyal' , 'ahsan'}
heart_react:set = {'abdulahh' , 'haseeb'}
all = wow_react | laugh_react | heart_react 
print(all)


# Intersection (common elements)
# apple
summer_fruits: set = {'apple' , 'banana' , 'mango'}
winter_fruits: set = {'oranges' , 'apple' , 'annar'}

common_fruits = summer_fruits.intersection(winter_fruits)
print(common_fruits)



winter_fruits: set = {'oranges' , 'apple' , 'annar'}
if 'oranges' in winter_fruits:
    print('oranges')

if 'mango' not in winter_fruits:
    winter_fruits.add()

lunch = {'bhindi'}
if 'bhindi' in lunch:
    lunch.discard()



# For Loops (when you know the ending point)
# The following example is add to cart feature.
# Think yourself as a superstore customer.
# After shopping you will be charged the amount of the products you have purchased.
# Price of each product is added to the total
cart: list = [
    {'product': 'shoes' , 'price': 39},
    {'product': 'Tshirt' , 'price': 99},
    {'product': 'hat' , 'price': 59},
    {'product': 'socks' , 'price': 11},

]

total: int = 0
for kharcha in cart:
    total = total + kharcha['price']

print(total)

# While loop (executed till the certain condition is True)
# Think of yourself as a men who is doing the activity of scanning the price of the Product
# The duty of the men is to scan the price of all the products in the basket.
# When the items in the basket ends the condition becomes false and the program ends
total = 0
while True:
    price_input: str = input("Enter the price of the Product ")

    if price_input == 'done':
        break

    if price_input.isdigit():
        total += int(price_input)
        print("Current total:", total)