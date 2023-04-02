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

my_dog = Dog("Buddy", 3, "Golden Retriever")
print(f"{my_dog.name} is {my_dog.age} years old and is a {my_dog.breed}.")
my_dog.speak()
