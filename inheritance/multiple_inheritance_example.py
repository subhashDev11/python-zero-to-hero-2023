class Flyer:
    def fly(self):
        print("I can fly!")

class Swimmer:
    def swim(self):
        print("I can swim!")

class Bird(Flyer, Swimmer):
    pass

class Fish(Swimmer, Flyer):
    pass

bird = Bird()
fish = Fish()

bird.fly()
bird.swim()

fish.swim()
fish.fly()
