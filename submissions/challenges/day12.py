class Person:
    def __init__(self, name, fave_subject, fave_food):
        self.name = name
        self.fave_subject = fave_subject
        self.fave_food = fave_food

name = input("Please enter your name: ")
food = input("Please enter your fave food: ")
subject = input ("Please enter your fave subject: ")
person = Person(name, subject, food)

print(f"\n{person.name}'s fave subject is {person.fave_subject}")
print(f"{person.name}'s fave food is {person.fave_food}.")