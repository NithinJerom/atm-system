pin = "1234"
attempts = 3
balance = 10000
history = []

while attempts > 0:
    user_pin = input("Enter your 4-digit PIN: ")

    if user_pin == pin:
        print("\n===================================")
        print("      LOGIN SUCCESSFUL!")
        print("      Welcome to ATM")
        print("===================================")

        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Your balance is: ₹", balance)

            elif choice == "2":
                amount = float(input("Enter amount to deposit: ₹"))

                if amount > 0:
                    balance += amount
                    history.append(f"Deposited ₹{amount}")
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
                    balance -= amount
                    history.append(f"Withdrew ₹{amount}")
                    print("Please collect your cash.")
                    print("Remaining balance: ₹", balance)

            elif choice == "4":
                current_pin = input("Enter current PIN: ")

                if current_pin == pin:
                    new_pin = input("Enter new 4-digit PIN: ")

                    if len(new_pin) == 4 and new_pin.isdigit():
                        pin = new_pin
                        print("PIN changed successfully!")
                    else:
                        print("PIN must be exactly 4 digits.")

                else:
                    print("Incorrect current PIN!")

            elif choice == "5":

                if len(history) == 0:
                    print("No transactions yet.")

                else:
                    print("\n===== Transaction History =====")

                    for transaction in history:
                        print(transaction)

            elif choice == "6":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice! Please enter a number between 1 and 6.")

        break

    else:
        attempts -= 1

        if attempts > 0:
            print("Incorrect PIN!")
            print("Attempts left:", attempts)
        else:
            print("Too many incorrect attempts.")
            print("Your account has been locked!")