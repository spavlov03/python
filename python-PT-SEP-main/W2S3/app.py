# OOP Pillar

## 1) Encapsulation


class User:
    def __init__(self, first_name, last_name, email, password=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def get_user_info(self):
        print(f"userName: {self.first_name} {self.last_name}")


# 2) Inheritance
# Student is a sub-class of User
class Student(User):
    def __init__(self, first_name, last_name, email, password, stack):
        # super ===>> User
        # WE HAVE TO INVOKE THE __INIT__ of the super class
        super().__init__(first_name, last_name, email, password)
        self.stack = stack
        self.belt = None

    # 3) Polymorphism
    def get_user_info(self):
        if self.stack == "Python":
            print("__PYTHON__")
        else:
            print(f"Oh Well {self.stack} 🧐😑")

    def submit_exam(self, grade, time):
        # related to #4
        self.belt = Belt.get_belt(grade, time)
        return self.belt


# 4) Abstraction


class Belt:
    def __init__(self):
        pass

    @staticmethod
    def get_belt(grade, time):
        if time <= 5:
            if grade > 9.49:
                return "Black Belt"
            elif grade > 8 and grade < 9.49:
                return "RED Belt"
            else:
                return "NO PASS"
        elif time > 5 and time <= 24:
            if grade > 8:
                return "ORANGE BELT"
            else:
                return "NO PASS"
        else:
            return "NO PASS"


user = User("John", "Doe", "j@j.com", "123456")

user.get_user_info()

student = Student("Jane", "Doe", "j@j.com", "123456", "MERN")

student.get_user_info()

print(student.submit_exam(9.5, 25))
print(student.submit_exam(9, 4))
print(student.submit_exam(9.5, 3))
