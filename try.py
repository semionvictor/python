try:
    name = input("Enter your name: ")
    while True:
        try:
            age = int(input("enter your age: "))
            break
        except ValueError:
            print("Enter a valid age")
    while True:
        try:
            grade = float(input("enter your achool grade "))
            break
        except ValueError:
            print("Enter a valid grade")
    
    with open('mm.txt', 'a') as file:
        file.write(f'my name is {name}, age is {age}, grade is {grade}')

except Exception as e:
    print(f'an error occured: {e}')