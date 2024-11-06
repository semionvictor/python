try:
    fileName = input("enter file name")
    with open(fileName,"r")as  file:
       print(file.read())
except FileNotFoundError:
     print("file does not exist")
    
    