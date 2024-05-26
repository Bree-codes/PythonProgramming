#This is a simple ATM code using If statements

initial_balance = 5000.00

def display_menu():
    print(f"Welcome to the display page!")
    print(f"1.Deposit to your account")
    print(f"2.Withdraw from your account")
    print(f"3.Check your account balance")
    print(f"4.Exit")
    
while True:
    display_menu()
    choice = int(input("Enter your choice: "))

    if(choice == 1):

        amount = float(input("Enter amount to deposit: "))

        if(amount > 0):

            balance = amount + initial_balance

            print(f"ksh{amount} deposited successfully!")
            print(f"Your account balance is ksh{balance}")


    elif(choice == 2):

        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

        if(withdrawal_amount <= initial_balance):
            current_balance = initial_balance- withdrawal_amount

            print(f"You have successfully withdrawn ksh{withdrawal_amount}")
            print(f"Your current account balance is ksh{current_balance}")

        else:
            print("Insufficient funds.")

    elif(choice == 3):

        print(f"Your account balance is ksh{initial_balance}")

    elif(choice == 4):

        # Exit
        print("Thank you for using the Simple ATM. Goodbye!")

        break

    else:

      print("Invalid choice. Please select a valid option.")

