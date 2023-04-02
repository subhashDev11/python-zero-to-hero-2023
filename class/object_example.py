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

person1 = Person("Brij", 20)

print(person1.name)
print(person1.age)
person1.say_hello()

person2 = Person("Ashish", 5)
print(person2.name)
print(person2.age)
person2.say_hello()
