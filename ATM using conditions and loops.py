def simple_atm():
    balance = 1000  
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
       
        
        choice = int(input("Enter your choice (1/2/3/4): "))

        
        if choice == 1:
            print(f"Your balance is: ${balance}")

        elif choice == 2:
            deposit = float(input("Enter deposit amount: $"))
            balance += deposit
            print(f"You deposited: ${deposit}. Your new balance is: ${balance}")

        elif choice == 3:
            withdraw = float(input("Enter withdrawal amount: $"))
            if withdraw <= balance:
                balance -= withdraw
                print(f"You withdrew: ${withdraw}. Your new balance is: ${balance}")
            else:
                print("Insufficient balance!")

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break  

        else:
            print("Invalid choice, please try again.")


simple_atm()



OUTPUT 
ATM Menu:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Enter your choice (1/2/3/4): 1
Your balance is: $1000

ATM Menu:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Enter your choice (1/2/3/4): 2
Enter deposit amount: $50000
You deposited: $50000.0. Your new balance is: $51000.0

ATM Menu:
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
Enter your choice (1/2/3/4): 3
Enter withdrawal amount: $2000
You withdrew: $2000.0. Your new balance is: $49000.0
