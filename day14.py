class Dog:
    sound = "bark"

dog1 = Dog()
print(dog1.sound)

class Dog:
    species = "canine"

    def __init__(self,name,age):
        self.name = name

        self.age = age 

dog1 = Dog("Buddy",3)

print(dog1.age)
print(dog1.species)

class Cat:


    def __init__(self,name,colour,eyecolour):
        self.name = name
        self.colour = colour
        self.eyecolour = eyecolour

    def meow(self):
        print(f"{self.name} is meow! and it is {self.colour}in colour")

cat1 = Cat("sweety","black","blue")
cat1.meow()