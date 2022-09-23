class Student:
    # class Attribute
    school = "Coding Dojo"
    stacks = ["Python", "MERN", "JAVA", "C#"]
    # constructor / init method
    def __init__(self, first_name, last_name, age):
        # self represent the instance of the class
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_ninja = False
        # self.gpa = 0

    def __str__(self):
        return f"THE NAME is {self.first_name} {self.last_name} AGE: {self.age}"

    # instance methods need to have self as a param
    def say_name(self):
        # self will have all the attributes defined in __init__
        print(f"My Name is: {self.first_name} {self.last_name}")

    def get_older(self):
        self.age += 1
        return self

    def get_age(self):
        return self.age

    def update_flag(self):
        # in python not === !
        # not True => False
        # not False => True
        # self.is_ninja = True
        self.is_ninja = not self.is_ninja

    @classmethod
    def is_valid_stack(cls, stack):
        print("THE CLASS", cls)
        if stack in cls.stacks:
            return True
        else:
            return False

    @staticmethod
    def validate_age(age):
        if age >= 18:
            return True
        return False


# create class instance (Object)

john = Student("John", "Doe", 30)
jane = Student("Jane", "Doe", 20)

john.say_name()


print(john.get_older().get_age())
print(john)
print(Student.school)
print(Student.is_valid_stack("dfsfd"))
print(john.is_valid_stack("dfsfd"))
# print(student1.school)

age = 19

if Student.validate_age(age):
    test = Student("Test", "Doe", age)
    print(test)
else:
    print("AGE IS LESS THAN 18!!!")
