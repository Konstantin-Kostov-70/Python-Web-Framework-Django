class Person:
    def __init__(self, first_name, age, last_name=''):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name} Age: {self.age}"


person = Person('Pesho', 23)
print(person)

person = Person('Pesho', 23, 'Peshev')
print(person)


class Student:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age

    def __str__(self):
        attributes = [f"{attr}: {getattr(self, attr)}" for attr in dir(self) if not attr.startswith('__')]
        return f"Student: {', '.join(attributes)}"


student = Student('John', 30)
print(student)

setattr(student, 'last_name', 'Doe')
# two options to set new attribute to student
# setattr(student, 'occupation', 'Engineer')
student.occupation = 'Engineer'

print(student)
