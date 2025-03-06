class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.stuff_in_belly = 0
        self.position = 0
    def talk(self):
        return f"{self.name} says {self.talk()}"
    def walk(self, stuff_in_belly):
        stuff_in_belly -= 1
        return f"{self.name} has moved"
    def run(self, stuff_in_belly):
        stuff_in_belly -= 2
        return f"{self.name} is fast as fuck boy"
    def is_hungry(self):
        if self.stuff_in_belly == 0:
            return f"{self.name} is hungry"
    def poop(self):
        if self.stuff_in_belly > 5:
            self.stuff_in_belly -= 3
            return f"{self.name} pooped"
        
    def eat(self, amount):
        self.stuff_in_belly += amount
        if self.stuff_in_belly > 5:
            return self.poop()
        return f"{self.name} has eaten {amount} units of food"
    
class Dog(Animal):
    def talk(self):
        return f"{self.name} says Woof!"
    def fetch(self):
        return "I'm fetching"
    
class Sheep(Animal):
    def talk(self):
        return f"{self.name} says Baa!"

class Pig(Animal):
    def talk(self):
        return f"{self.name} says Oink!"
    
    
pig = Pig("biggetje", "bruin")
print(pig.talk())
print(pig.eat(1))
dog = Dog("Blacky", "wit")
print(dog.talk())
print(dog.fetch())
sheep = Sheep("Shaun", "zwart")
print(sheep.talk())