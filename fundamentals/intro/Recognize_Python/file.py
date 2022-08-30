num1 = 42 #- variable declaration
num2 = 2.3 #- variable declaration
boolean = True #- variable declaration
string = 'Hello World' #- variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #- variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #- variable declaration
fruit = ('blueberry', 'strawberry', 'banana') #- variable declaration
print(type(fruit)) #- log statement
print(pizza_toppings[1]) #- log statement
pizza_toppings.append('Mushrooms') #- Data Types - Composite - List - add value
print(person['name']) #- log statement
person['name'] = 'George' #- Data Types - Composite - Dictionary - change value
person['eye_color'] = 'blue' #- Data Types - Composite - Dictionary - add value
print(fruit[2]) #- log statement

if num1 > 45: #- conditional - if
    print("It's greater") #- log statement
else: #- conditional - else
    print("It's lower") #- log statement

if len(string) < 5: #- conditional - if
    print("It's a short word!") #- log statement
elif len(string) > 15: #- conditional - else if
    print("It's a long word!") #- log statement
else: #- conditional - else
    print("Just right!") #- log statement

for x in range(5): #- for loop
    print(x) #- log statement
for x in range(2,5): #- for loop
    print(x) #- log statement
for x in range(2,10,3): #- for loop
    print(x) #- log statement
x = 0 #- variable declaration
while(x < 5): #- while loop - start
    print(x) #- log statement
    x += 1 #- while loop - increment

pizza_toppings.pop() #- Data Types - Composite - List - delete value
pizza_toppings.pop(1) #- Data Types - Composite - List - delete value

print(person) #- log statement
person.pop('eye_color') #- Data Types - Composite - Dictionary - delete value
print(person) #- log statement

for topping in pizza_toppings: #- for loop - start
    if topping == 'Pepperoni': #- conditional - if
        continue #- for loop - continue
    print('After 1st if statement') #- log statement
    if topping == 'Olives': #- conditional - if
        break #- conditional - stop

def print_hello_ten_times(): #- function
    for num in range(10): #- function - parameter - for loop
        print('Hello') #- for loop - log statement

print_hello_ten_times() #- function

def print_hello_x_times(x): #- function
    for num in range(x): #- function - parameter - for loop
        print('Hello')

print_hello_x_times(4) #- function

def print_hello_x_or_ten_times(x = 10): #- function
    for num in range(x): #- function - parameter - for loop
        print('Hello') #- for loop - log statement

print_hello_x_or_ten_times() #- function
print_hello_x_or_ten_times(4) #- function


"""
Bonus section
"""

print(num3) #- NameError: name <num3> is not defined
num3 = 72 
fruit[0] = 'cranberry' #- TypeError: 'tuple' object does not support item assignment
print(person['favorite_team']) #- KeyError: 'favorite_team'
print(pizza_toppings[7]) #- IndexError: list index out of range
  print(boolean) #- IndentationError: unexpected indent
fruit.append('raspberry') #- AttributeError: 'tuple' object has no attribute 'append'
fruit.pop(1) #- AttributeError: 'tuple' object has no attribute 'pop'