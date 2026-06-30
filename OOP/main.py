class ATM:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            user_input = input("""
Hello! How would you like to proceed?

1. Create PIN
2. Change PIN
3. Check Balance
4. Deposit Money
5. Withdraw Money
6. Exit

Enter your choice:
""")

            if user_input == "1":
                self.create_pin()

            elif user_input == "2":
                self.change_pin()

            elif user_input == "3":
                self.check_balance()

            elif user_input == "4":
                self.deposit()

            elif user_input == "5":
                self.withdraw()

            elif user_input == "6":
                print("Thank you for using our ATM.")
                break

            else:
                print("Invalid Option! Please try again.")

    def create_pin(self):
        self.pin = input("Enter a new PIN: ")
        print("PIN created successfully!")

    def change_pin(self):
        old_pin = input("Enter your current PIN: ")

        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("PIN changed successfully!")
        else:
            print("Incorrect PIN!")

    def deposit(self):
        pin = input("Enter your PIN: ")

        if pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Incorrect PIN!")

    def check_balance(self):
        pin = input("Enter your PIN: ")

        if pin == self.pin:
            print(f"Your balance is ₹{self.balance}")
        else:
            print("Incorrect PIN!")

    def withdraw(self):
        pin = input("Enter your PIN: ")

        if pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
                print(f"Remaining Balance: ₹{self.balance}")
            else:
                print("Insufficient Balance!")
        else:
            print("Incorrect PIN!")


atm = ATM()