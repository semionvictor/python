class Animal():
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def eat(self):
            print("the animal is eating")
    def walk(self):
        print("the animal is walking")

class Bird(Animal):
    def __init__(self, name, color, beak_color):
        print("a new bird was created")
        super().__init__(name, color)
        self.beak_color = beak_color

    def eat(self):
        super().eat()
        print("this is a bird")

    def fly(self)  :
        print("the bird is flying") 
    
    
eagle = Bird("eagle","white","beak_color")
eagle.eat()
eagle.fly()
print(eagle.name)


