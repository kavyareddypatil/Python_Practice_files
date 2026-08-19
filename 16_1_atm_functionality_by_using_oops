class ATM():
    def __init__(self,balance=0):
        self.balance = balance
        self.ministatement = []
class atm_operations(ATM):
    def credit_amount(self,):
        amount = float(input("Enter amount to credit : "))
        if amount <= 0:
            print("Invalid amount, enter positive number.")
        else:
            self.balance += amount
            self.ministatement.append(f"Credited amount: {amount:.2f}")
            print(f"Amount credited successfully")
            print(f"{amount:.2f} credited to your account.")

    def debit_amount(self,):
        amount = float(input("Enter amount to debit:"))
        if amount <= 0:
            print("Invalid amount, enter only positive number.")
        elif self.balance < amount:
            print("Insufficient balance. Please enter amount lessthan or equal of balance.")
            print(f"Balance is {self.balance:.2f} and entered amount is {amount:.2f}")
        else:
            self.balance -= amount
            self.ministatement.append(f"Debited amount : {amount:.2f}")
            print("Amount debited successfully..")
            print(f"{amount:.2f} debited from your account")

    def check_balance(self,):
        print(f"Available Balnce :{self.balance:.2f}")

    def mini_statement(self,):
        print("\n----------MINI STATEMENT-----------")
        if len(self.ministatement) == 0:
            print("No trasactions found")
        else:
            for i in self.ministatement:
                print(i)

        print(f"Available balance : {self.balance:.2f}")
    
    

atm = atm_operations()
def menu():
    while True:
        print("\n ATM MENU")
        print("1.Credit")
        print("2.Debit")
        print("3.Check Balance")
        print("4.Mini statemnet")
        print("5.Exit")
        choice = input("Enter your choice : ")
        if choice == "1":
            atm.credit_amount()
        elif choice == "2":
            atm.debit_amount()
        elif choice == "3":
            atm.check_balance()

        elif choice == "4":
            atm.mini_statement()
        elif choice == "5":
            print("thank for using ATM..")
            break
        else:
            print("Invalid choice. Please enter choice between 1 to 5")  
menu()      

