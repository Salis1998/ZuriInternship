"""""""""
1. Use functions

2. Include register, and login

3. Generate Account Number

4. Any other improvement you can think of (extra point)
"""""""""""
import random
import databases
import validation
from datetime import datetime
from getpass import getpass


today = datetime.today()
print("Today's date is:",today)
print("********** Welcome to our Bank Application ***********")

def init():
    print("[1] login")
    print("[2] register")
    option =int(input("Select an Option so that we can help you! \n"))

    if option == 1:
        login()

    elif option == 2:
        register()

    else:
        print("Invalid Option")
        init()

def login():
    print("'Login to you Account")

    accnumber=input("what is you account number?")
    is_valid_accnumber = validation.accnumber(accnumber)

    if is_valid_accnumber:
        password = getpass("Enter your password \n")
        user = databases.authenticated_user(accnumber,password);

        if user:
            bank_operation(user)
        print("Invalid account or password")
        login()

    else:
        print("Invalid Account number")
        init()

        login()

def register():
    print("Register your Account")
    email = input("What is your email address? \n")
    fname = input("What is your first name? \n")
    lname = input("What is your last name? \n")
    password = getpass("What is your the password of your choice? \n")

    accnumber = generate_accnumber
    is_user_created = databases.create(accnumber,fname,lname,email,password)

    if is_user_created:
        print("Account has been created")
        print("")
        print("Your Account number is: %d" % accnumber)
        login()
    else:
        print("Something went wrong")

        register()

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    print("[1] Withdraw")
    print("[2] Deposit")
    print("[3] logout")
    print("[0] Exit")

    selected_option = int(input("Select an option such that we can help you!"))

    if selected_option == 1:
        withdraw_operation()

    elif selected_option == 2:
        deposit_operation()

    elif selected_option == 3:
        logout_operation()

    elif selected_option == 4:
        exit_operation()

    else:
        print("You have selected an invalid option")
        bank_operation(user)





def generate_accnumber():
    return random.randrange(1111111111, 9999999999)
    generate_accnumber()

def withdraw_operation():
    balance =1500
    print("Withdraw operation")
    print("Your Current Balance is: ", balance)
    a = float(input("Enter the amount you want to Withdraw: "))
    if a > balance:
        print("Not allowed to withdraw:", a)
    else:
        balance = balance - a
        print("Take your cash:", a)
        print("Your new balance is", balance)
        withdraw_operation()

def deposit_operation():
    balance = 1500
    print("Deposit operation")
    print("Your Current Balance is: ", balance)
    b = float(input("Enter the amount you want to Deposit: "))
    balance = balance + b
    print("You have successfully deposited: ", b)
    print("Your new balance is: ", balance)
    deposit_operation()

def logout_operation():
    print("press any key to exit!")
    login()

def exit_operation():
    print("")
    login()
init()
