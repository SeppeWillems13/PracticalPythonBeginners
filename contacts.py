contacts = {
    "number": 4,
    "students":
    [
        {"name": "John", "phone": "555-1234"},
        {"name": "Mary", "phone": "555-5678"},
        {"name": "Bob", "phone": "555-9012"},
        {"name": "Alice", "phone": "555-3456"}
    ]
}

for student in contacts["students"]:
    print(student["name"], student["phone"])