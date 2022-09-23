# 11
b = 500
print("THIS IS THE FIRST ONE", b)


def foobar():
    b = 300
    print("THIS IS INSIDE FOOBAR", b)
    return b


print("THIS ONE IS BEFORE", b)
# b = foobar()
print("THIS IS THE ONE!!!", foobar())
print("THIS ONE IS AFTER", b)
# print(foobar)

list = [1, 2, 3, 4]
print(list.reverse())
list.reverse()  # returns None
print(list)
print("__________")
students = [
    {"name": "test1", "age": 21, "stacks": ["python", "MERN", "JAVA"]},
    {"name": "test2", "age": 40, "stacks": ["MERN", "python" "JAVA"]},
    {"name": "test3", "age": 20, "stacks": ["MERN", "JAVA"]},
    {"name": "test4", "age": 50, "stacks": ["python"]},
]

# print the name of each student and all the stacks for that student
# print(students["name"]["stacks"])

for student in students:
    print("THE student IS???", student["name"])
