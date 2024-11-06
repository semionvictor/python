# try:
#     file = open('files.p')
#     print(file.read())
# except FileNotFoundError:
#     print('File does not exist')
    
# file.close()

# with open('files.p') as file:
#     print(file.read())


# with open("home.txt", "w") as file:
#     text = "\n I am a boy"
#     # print(file.append(text))\
#     print(file.write(text))

# print("enter file name")
# file_name = input()

# def read_file(file_name):
#     file_exist = file_name
#     if file_exist:
#         file = open(file_name, "r")
#         file.close()
#         return True 
#     else:
#         return False
    
# reader = read_file(file_name)
# print(reader)


import oop_calculator

calc = oop_calculator.Calculator(2, 4, '-')
print(calc.subtract())
