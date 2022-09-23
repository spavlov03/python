# THE OUTPUT OF
# SELECT * FROM students;
students = [
    {"id": 1, "name": "test", "email": "t@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
    {"id": 2, "name": "john", "email": "t@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
    {"id": 3, "name": "jack", "email": "t@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
    {"id": 4, "name": "jane", "email": "t@t.com", "created_at": "1232q3213", "updated_at": "1232q3213"},
]


class Student:
    # data is a dict [id,name....]
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def __repr__(self):
        return self.name


all_students = []
for student in students:
    one_student = Student(student)
    all_students.append(one_student)

print("######ALL STUDENTS", all_students)
