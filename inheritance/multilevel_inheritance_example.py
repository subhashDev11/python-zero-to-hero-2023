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

class WorkingDog(Dog):
    def __init__(self, name, age, breed, job):
        super().__init__(name, age, breed)
        self.job = job

    def speak(self):
        print("Working dog barks louder!")

my_dog = WorkingDog("Buddy", 3, "Golden Retriever", "Guide dog")
print(f"{my_dog.name} is {my_dog.age} years old and is a {my_dog.breed}.")
print(f"{my_dog.name} is a {my_dog.job}.")
my_dog.speak()
