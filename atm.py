pin = "1234"
attempts = 3

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        print("Login Successful!")

        balance = 10000

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your balance is: ₹", balance)

            elif choice == "2":
                amount = float(input("Enter amount to deposit: ₹"))

                if amount > 0:
                    balance = balance + amount
                    print("₹", amount, "deposited successfully.")
                    print("New balance: ₹", balance)
                else:
                    print("Please enter a valid amount.")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: ₹"))

                if amount <= 0:
                    print("Please enter a valid amount.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance = balance - amount
                    print("Please collect your cash.")
                    print("Remaining balance: ₹", balance)

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        break

    else:
        attempts = attempts - 1

        if attempts > 0:
            print("Incorrect PIN!")
            print("Attempts left:", attempts)
        else:
            print("Too many incorrect attempts.")
            print("Your account has been locked!")