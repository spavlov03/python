students = [
    {"name":"test1", "age":21, "stacks": ["python", "MERN", "JAVA"], "status": {"is_active": True }},
    {"name":"test2", "age":22, "stacks": ["python", "MERN", "JAVA"], "status": {"is_active": False}},
    {"name":"test3", "age":23, "stacks": ["python", "MERN", "JAVA"], "status": {"is_active": False}},
    {"name":"test4", "age":24, "stacks": ["python", "MERN", "JAVA"], "status": {"is_active": True }},
]

for student in students:
    print(student["name"])
    for stack in student["stacks"]:
        print(stack)
    print(student["status"]."is_active")