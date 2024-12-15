class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance

    def authenticate(self, entered_pin):
        if self.pin == entered_pin:
            print("Authentication successful!\n")
            return True
        else:
            print("Authentication failed! Incorrect PIN.\n")
            return False

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}\n")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You have successfully deposited ${amount:.2f}.")
            self.check_balance()
        else:
            print("Deposit amount must be greater than zero.\n")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"You have successfully withdrawn ${amount:.2f}.")
                self.check_balance()
            else:
                print("Insufficient balance!\n")
        else:
            print("Withdrawal amount must be greater than zero.\n")


def main():
    print("Welcome to the ATM Interface!\n")

    # Initialize the ATM with a default PIN and balance
    user_atm = ATM(pin="1234", balance=500.00)

    # Simulate the ATM interface loop
    attempts = 3
    authenticated = False

    while attempts > 0 and not authenticated:
        entered_pin = input("Enter your 4-digit PIN: ")
        authenticated = user_atm.authenticate(entered_pin)
        if not authenticated:
            attempts -= 1
            print(f"Attempts remaining: {attempts}\n")

    if not authenticated:
        print("Too many incorrect attempts. Exiting.\n")
        return

    while True:
        print("\nChoose an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            if choice == 1:
                user_atm.check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                user_atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                user_atm.withdraw(amount)
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!\n")
                break
            else:
                print("Invalid choice. Please select a valid option.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

if __name__ == "__main__":
    main()
