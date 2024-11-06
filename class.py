class Animal ():
    def __init__(self, nameArg, colorArg, noOfLegsArg ): 
        self.color = colorArg
        self.name = nameArg
        self.noOfLegs = noOfLegsArg
        print(self.color)

        # print(f"created a new animalobject with characteristics of name:{nameArg},color:{colorArg}, and noOfLegs: {noOfLegsArg}")
    
    def walk(self):
        pass



objOne = Animal("Rat", "White", 4)
objTwo = Animal("Bird", "Brown",2)
    