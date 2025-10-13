#single inheritence
class parent:
    def greet(self):
        print("Hello from parent!")

class child(parent):
    def greet_child(self):
        print("Hello from child")

c = child()
c.greet()
c.greet_child()

#multiple inheritance
class father:
    def skill(self):
        print("father: knows driving")

class mother:
    def hobby(self):
        print("mother: loves cooking")

class child(father, mother):
    def talent(self):
        print("child: plays guider")


c = child()
c.skill()
c.hobby()
c.talent()

#multiple level inheritances
class Grandparent:
    def greet_gp(self):
        print("hello from grandparent!")

class parent(Grandparent):
    def greet_parent(self):
        print("Hello from parent!")

class child(parent):
    def greet_child(self):
        print("Hello from child!")

class Grandchild(child):
    def greet_gc(self):
        print("Hello from Grandchild!")



c = Grandchild()
c.greet_gp()
c.greet_parent()
c.greet_child()
c.greet_gc()

#Hierarchial inheritence
class Animal:
    def sound(Self):
        print("Animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class cat(Animal):
    def sound(self):
        print("Cat meows")

d = Dog()
c = cat()
d.sound()
c.sound()

#Hybrid inheritance
class A:
    def showA(self):
        print("class A")

class B(A):
    def showB(self):
        print("class B")

class C(A):
    def showC(self):
        print("class c")

class D(B,C):
    def showD(self):
        print("class D")

obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()


#polymorphism
class Dog:
    def sound(self):
        return "Barks"

class Cat: 
    def sound(self):
        return "Meows"

for animal in (Dog(),Cat()):
      print("barks","Meows")


class Bird:
    def fly(self):
        print("Birds can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly")

p = Penguin()
p.fly()

#Encapsulation
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("invaild withdrawal amount")


acc = BankAccount("12345",1000)
print(acc.account_number)
print("Current Balance:", acc.get_balance())
acc.deposit(500)
acc.withdraw(300)
print("Final Balance:", acc.get_balance())





    