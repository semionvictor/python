# collect first input
# collect operation sign
# collect second input
# operate on inputs using the sign
# 4.1 if operation sign is addition (add)
# 4.2 if operation sign is * (multiply)
# 4.

print("enter first number")
first_number = input()

print("enter operation")
operation_sign = input()

print("enter second number")
second_number = input()

def add(numberOne, numberTwo):
    return int(numberOne) + int(numberTwo)

def multiply(numberOne, numberTwo):
    return int(numberOne) * int(numberTwo)

def subtract(numberOne, numberTwo):
    return int(numberTwo) - int(numberOne)

def divide(numberOne, numberTwo):
    return int(numberTwo) / int(numberOne)

allowed_operation = ["+", "-" ,"*" "/"]

if (operation_sign not in allowed_operation):
    print(f"operation{operation_sign} is not allowed")
else:

    if(operation_sign == "+"):
        # add
        result = add(first_number, second_number)
        print(f"result of {first_number} {operation_sign} {second_number} is {result}")
        
    elif(operation_sign == "*"):
        # multiply
        result = multiply(first_number, second_number)
        print(f"result of {first_number} {operation_sign} {second_number} is {result}")
        
        
    elif(operation_sign == "-"):
        # subtract
        result = subtract(first_number, second_number)
        print(f"result of {first_number} {operation_sign} {second_number} is {result}")

        
    else:
        # divide
        result = divide(first_number, second_number)
        print(f"result of {first_number} {operation_sign} {second_number} is {result}")

        
