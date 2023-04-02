class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Animal speaks!")

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Dog barks!")

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Cat meows!")

my_dog = Dog("Buddy", 3, "Golden Retriever")
my_cat = Cat("Fluffy", 2, "White")
print(f"{my_dog.name} is {my_dog.age} years old and is a {my_dog.breed}.")
print(f"{my_cat.name} is {my_cat.age} years old and is {my_cat.color}.")
my_dog.speak()
my_cat.speak()
