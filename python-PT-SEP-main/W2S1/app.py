# OOP????
# Object Oriented Programming
# Class???

# student1 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student2 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student3 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student4 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student5 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student6 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student7 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}
# student8 = {"first_name": "John", "last_name": "Doe", "age": 20, "is_ninja": False}


# def update_age(student, age):
#     student["age"] = age


# update_age(student1, 30)

# print(student1["age"])


class Student:
    # constructor / init method
    def __init__(self, first_name, last_name, age):
        # self represent the instance of the class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_ninja = False
        # self.gpa = 0

    # instance methods need to have self as a param
    def say_name(self):
        # self will have all the attributes defined in __init__
        print(f"My Name is: {self.first_name} {self.last_name}")

    def get_older(self):
        self.age += 1
        return self.age

    def update_flag(self):
        # in python not === !
        # not True => False
        # not False => True
        # self.is_ninja = True
        self.is_ninja = not self.is_ninja


# create class instance (Object)

student1 = Student("John", "Doe", 30)
student2 = Student("Jane", "Doe", 20)
print(student1.first_name)

student1.say_name()
student2.say_name()

student_age = student1.get_older()
student1.update_flag()
student1.update_flag()
print("ISNINJA????", student1.is_ninja)
print(student1.age)
print(student2.age)
if student_age > 18:
    print("OK")

if student1.age > 18:
    print("OK")
