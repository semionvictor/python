print('Enter the path to the file you want to read')
file_path = input()
correct_path = file_path.replace('\\', '/')

print(correct_path)
file = open(correct_path,"C:/Users/user/OneDrive/Desktop/PYTHON/name.txt", 'w')

data = ["first line \n","second line \n","third line \n"]
print('=====   THE CONTENTS OF YOUR FILE =====')
