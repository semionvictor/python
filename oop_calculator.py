class Calculator:


    def __init__(self, numberOne, numberTwo, operation_sign):
        self.num1 = int(numberOne)
        self.num2 = int(numberTwo)
        self.operationSign = operation_sign
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
    def calculate(self):
        if self.operationSign == "+":
            result = self.add()
            return result
        elif self.operationSign == "-":
            result = self.subtract()
            return result
        elif self.operationSign == "*":
            result = self.multiply()
            return result
        elif self.operationSign == "/":
            result = self.divide()
            return result
        else:
            return "operation not allowed"
    



# print("enter number one")
# numberOne = input()

# print("enter operation sign")
# operation_sign = input()

# print("enter number two")
# numberTwo = input()

# calculator = Calculator (numberOne, numberTwo, operation_sign)
# output = calculator.calculate()
# print(output)
