class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says hello!")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print(f"{self.name} barks!")
my_dog = Dog("Buddy")
my_dog.speak()  # output: Buddy barks!
