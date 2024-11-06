#create account 
#deposit
#withdraw
#transfer 
#check 

class User():
    def _init_(self, name, email, password):
        self.name = name
        self.email = email
        self.password= password

class BankAccount():
    def _init_(self, balance, account_number, user_name):
        self.balance= balance
        self.account_number= account_number
        self.user_name = user_name

print('Welcome to the bank project, what would you like to do ')
print('1. Create a user account\n2. Login')
userChoice = input()

usersList = []

def login():
    print('====LOGIN====')
    print('Enter your username')
    username = input()

    print('Enter your password')
    password = input()
    def get_user(user):
        return user.name == username and user.password == password
    users = filter(get_user, usersList)
    print(list(users))

def create_user_account():
    print('=== CREATE YOUR USER ACCOUNT ===')
    print('Enter your name')
    name = input()
    
    print('Enter your email')
    email = input()

    print('Enter your password')
    password = input()
        
    user = User(name, email, password)
    usersList.append(user)
    login()
            
if userChoice == '1':
    create_user_account()
if userChoice == '2':
      login()
