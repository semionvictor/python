
import os
print('Enter the path to the file you want to write')
file_path = input()

print("enter your text ")
text = input()

corrected_path = file_path.replace("\\","/")


def write_file(file_path,text):
    file_exist = os.path.isfile(corrected_path)
    if file_exist:
        file = open(file_path,"w")
        file.write(text)
        file.close
        return True
    else:
        return False
    
written =  write_file(corrected_path,text)
print(written)
if written == True:
    print("write success")
else:
    print("failed to write")
# file = open(corrected_path,"w")

# dummy_text = "hello world"

# file.write(dummy_text)
# file.close()

