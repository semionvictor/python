# whrite two functions with the following functionalities.
# (1)a function that accept two argument(numberone,munbertwo)and returns the value of numberone minus numbertwo.?
# (2)a function that accepts two arguments(numberone,numbertwo)and returns the value of numberone multiply numbertwo.?

# def minus(numberone,munbertwo):
#     result = numberone-munbertwo
#     return result
# chiboy = minus(100,50)
# print(chiboy)


# def multiply(numberone,munbertwo):
#     result = numberone*munbertwo
#     return result
# chiboy = multiply(20,2)
# print(chiboy)
# def chiboy():
#     print("hes a big boy")
# chiboy()
# # passing an argument
# def chiboy(name):
#     print(name +" yes")
# chiboy("cup")
# chiboy("nice")
# def chiboy(*name):
#     print("the yungest child in our class is " + name[2])
# chiboy("kyrian","kingsley","swatt")



class House():

    # Passing different required arguments
    def __init__(self,noWindowsArg,colorArg,roofstyleArg) -> None:
        self.noWindowsArg = noWindowsArg
        self.color = colorArg
        self.roofStyle = roofstyleArg

        # Print the Arguments
        print(noWindowsArg)
        print(colorArg)
        print(roofstyleArg)
        print (F"a house has the{noWindowsArg} an {colorArg} and a {roofstyleArg} which makes the house more ")
    

    def build(self):
        print(f"building a {self.color} house with {self. noWindowsArg} windows, and has {self.roofStyle} roof style")


        # Calling for the class by defining an Object

houseOne = House(25,"orange","dutch roof")
print(houseOne.color)
houseTwo = House(30,"green","saltbox roof")

houseOne.build()