students = [
    {"name": "test1", "age": 21, "stacks": ["python", "MERN", "JAVA"], "status": {"is_active": True}},
    {"name": "test2", "age": 40, "stacks": ["MERN", "python", "JAVA"], "status": {"is_active": False}},
    {"name": "test3", "age": 20, "stacks": ["MERN", "JAVA"], "status": {"is_active": False}},
    {"name": "test4", "age": 50, "stacks": ["python"], "status": {"is_active": True}},
]

# print the name of each student and all the stacks for that student & the status of each student

# for element in students:
#     print("THE student IS???", element["name"], element["stacks"])
#     for stack in element["stacks"]:
#         print(stack)

## -------------------------
## Functions in python


def function_name():
    # function body
    pass


function_name()
# call or invoke the function
# DONT DO THIS "function_name"


def say_hi():
    print("Hi")


say_hi()


def greet(name):
    # name is a parameter
    print(f"Hello {name}")


# name will be the argument
greet("test")

print(greet("test1"))


def sum(a, b):
    return a + b


# y = sum
# print(y(4, 5))
print(type(sum), type(sum(1, 2)))
value = sum(4, 5)
print("Returned Value= ", value)


# conditional statements

age = 18

if age >= 90:
    print("cant drive :(")
elif age >= 18:
    print("can drive...🚗")
else:
    print("Not yet Kiddo...")


# create a function that will take in a integer as an input and return list contains all the numbers
# from 1 to that number if the number is divisible by 3 print fizz
# if its divisible by 5 print buzz
# if it divided by both print fizzbuzz
# return a list contain the output


def fizz_buzz(num):
    result = []
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(i)

    return result

# and == && , or == || not == !
the_result = fizz_buzz(30)  # [1,2,"fizz",4,"buzz",...14,"fizbuzz"]
print(the_result)
