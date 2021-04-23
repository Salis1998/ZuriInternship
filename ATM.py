from datetime import datetime
today = datetime.today()
print("Today's date is:",today)

name = input("Please Enter you name \n")
allowedUsers=["Salis","Ano","Tanya"]
allowedPassword=["password123"]

if(name in allowedUsers):
    password = input("Enter Your Password\n")
    if(password in allowedPassword):
        print("\nWelcome to the ATM Program :",name)        

        def menu():
            print("[1] Withdraw")
            print("[2] Deposit")
            print("[3] Complaint")
            print("[0] Exit")
            
        menu()
        option = int(input("Enter an Option so that we can assist you \n"))

        balance = 1500
        while option!=0:
            
            if option==1:
                print("Your Current Balance is: ", balance)
                a=float(input("Enter the amount you want to Withdraw: "))
                if a > balance:
                    print("Not allowed to withdraw:",a)
                else:
                    balance = balance -a
                    print("Take your cash:", a)
                    print("Your new balance is",balance)              
                
                menu()
                option = int(input("Enter an Option so that we can assist you \n"))


            elif option ==2:
                print("Your Current Balance is: ", balance)
                b=float(input("Enter the amount you want to Deposit: "))
                balance = balance + b
                print("You have successfully deposited: ", b)
                print("Your new balance is: ", balance)
                menu()
                option = int(input("Enter an Option so that we can assist you \n"))
                
            elif option==3:
                print("Your Current Balance is: ", balance)
                input("What Issue would you like to report:")
                print("Thank You for Contacting Us!")
                menu()
                option = int(input("Enter an Option so that we can assist you \n"))

            else:
                print("Invalid Option\nSelect an option from the menu")
                menu()
                option = int(input("Enter an Option so that we can assist you \n"))
               

        print("Thanks for using the ATM Program", name)        

    else:
        print("Incorrect Passwod, try again later")
else:
    print("User not found!")

