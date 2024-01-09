class Animal:
    def __init__(self, name):
        self.name = name
        print ("A new animal has been born")
        
    def eat(self):
        print ("Munch Munch")

    def make_noise(self):
        print ("Grr says", self.name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        print ("A new Cat has been born")

    def make_noise(self):
        print("Meow says", cat.name)

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
        print("A new dog has been born")

    def make_noise(self):
        print ("Bark Says", self.name)

cat = Cat("Harry")
cat.eat()
cat.make_noise()
print("-----------------------")

dog = Dog("KidRock")
dog.eat()
dog.make_noise()
print("-----------------------")

dog1 = Dog("Gian-Mari")
dog1.eat()
dog1.make_noise()
print("-----------------------")

animal = Animal("Ka-Istong")
animal.eat()
animal.make_noise()



