contacts = {
    "number": 4,
    "students": [
        {"name": "student1", "email": "student1@example.com"},
        {"name": "student2", "email": "student2@example.com"},
        {"name": "student3", "email": "student3@example.com"},
        {"name": "student4", "email": "student4@example.com"},
    ]
}

for student in contacts['students']:
    print(student['email'])