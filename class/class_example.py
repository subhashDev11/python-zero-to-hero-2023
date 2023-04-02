class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

person = Person("Subhash", 22)
print(person.name)
print(person.age)
person.say_hello()
