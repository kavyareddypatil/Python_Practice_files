balance = 0
mini_statement = []
def credit_amount():
    global balance
    amount = float(input("Enter amount to credit : "))
    if amount <= 0:
        print("Invalid input, amount cannot be zero or negative.")
    else:
        balance += amount
        mini_statement.append(f"Credited amount: {amount:.2f}")
        print("Amount credited successfully.")
        print(f"{amount:.2f} credited to your account.")

def debited_amount():
    global balance
    amount = float(input("Enter amount to debit : "))
    if amount <= 0:
        print("Invalid input, amount cannot be zero or negative.")
    elif amount > balance:
        print(f"Insufficient balance. {amount:.2f} exceeds {balance:.2f}")
    else:
        balance -= amount
        mini_statement.append(f"Debited amount : {amount:.2f}")
        print("Amount debited successfully.")
        print(f"{amount} debited from your account.")

def check_balance():
    print(f"Available balance : {balance:.2f}")


def show_mini_statement():
    print("\n----------MINI STATEMENT----------")
    if len(mini_statement) == 0:
        print("No transactions found.")
    else:
        for i in mini_statement:
            print(i)
    print(f"Available balance : {balance:.2f}")


def transaction_menu():
    while True:
        print("\n ATM Menu")
        print("1.Credit")
        print("2.Debit")
        print("3.Balance")
        print("4.Mini Statement")
        print("5.Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            credit_amount()
        elif choice == 2:
            debited_amount()
        elif choice == 3:
            check_balance()
        elif choice == 4:
            show_mini_statement()
        elif choice == 5:
            print("Thank for using the ATM..")
            break
        else:
            print("Invalid choice. Please enter choice between 1 to 5")
transaction_menu()
