class Student:
    def __init__(self, name, age, is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses

def get_input():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    is_enrolled = input("Is the student enrolled? (yes/no): ").lower() == 'yes'
    classes = input("Enter classes: ").split(',')
    offenses = input("Enter offenses: ").split(',')
    return name, age, is_enrolled, classes, offenses

students = []

while True:
    name, age, is_enrolled, classes, offenses = get_input()
    student = Student(name, age, is_enrolled, classes, offenses)
    students.append(student)
    
    add_more = input("Do you want to add another student? (yes/no): ").lower()
    if add_more != 'yes':
        break

for idx, student in enumerate(students, 1):
    print(f"\nStudent {idx}:")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Status: {'Enrolled' if student.is_enrolled else 'Not Enrolled Yet'}")
    print(f"Classes: {student.classes}")
    print(f"Offenses: {student.offenses}")