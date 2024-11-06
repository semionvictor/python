# file = open("C:/Users/user/OneDrive/Desktop/PYTHON/name.txt", "r")

# print(file.readline())#close the file and makes it available for other programs)#reads the first line of th file
# print(file.read())#reads the entire file



# print(file.readlines())

# file.seek(9)#moves the cursor to the 9th byte
# print(file.read())

# file.close()#close the file and makes it available for other programs


#                   2(w)

# file = open("C:/Users/user/OneDrive/Desktop/PYTHON/name.txt", "w")

# # file.write("this is the new line we are adding \n") #it write a single line

# data = ["first line \n","second line \n","third line \n"]

# file.writelines(data)




# file.close()





#             3(a)

file = open("C:/Users/user/OneDrive/Desktop/PYTHON/name.txt", "a")


data = ["first line \n","second line \n","third line \n"]


file.write("this is the new line we are adding \n")


