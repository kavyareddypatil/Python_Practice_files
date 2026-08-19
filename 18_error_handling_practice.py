'''Error handling
1.Syntax error or Compile time errors'''
#factorial of number
def factorial(num):
    fact = 1
    if num < 0 :
        return -1
    elif num == 0 or num == 1:
        return 1
    #for i in range(num+1) # SyntaxError: expected ':'
    for i in range(1,num+1):
        fact *= i
    return fact
#num = int(input("Enter a  number :") # SyntaxError: '(' was never closed
num = int(input("Enter a number : "))
print(factorial(num))


# # '''Another example for syntax error'''

first_name = input("Enter first name :")
last_name = input("Enter last name :")
full_name = first_name +" "+ last_name
#print("Full name : "full_name) # line 24 - SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("Full name :",full_name)



# '''2.Logical Errors'''
num_1 = int(input("Enter a number1 : "))
num_2 = int(input("Enter a number2 : "))
#addition = num_1 - num_2  
addition = num_1 + num_2
print("Addition of 2 numbers :",addition)
'''Output for the above code
Enter a number1 : 12
Enter a number2 : 14
Addition of 2 numbers : -2
'''
# It gives the output without any errors,the goal is addition of 2 numbers
# but it gives the different output
# this is  called logiacal errors.

#Bank Account example
class bank_account():
    def __init__(self,name,account_number,balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def credit(self,):
        amount = float(input("Enter amount to credit : "))
        if amount <= 0 :
            print("Amount cannot be zero or negative")
        else:
            #self.balance -= amount   
            '''the above line is logical error in this case 'we can add amount to the balance' but it withdraw amount from the account '''
            self.balance += amount
            print(f"Credited : {amount:.2f}")
            print(f"{amount:.2f} credited to your account successfully.")
    def debit(self,):
        amount = float(input("Enter amount to debit : "))
        if amount <= 0 :
            print("Amount cannot be zero or negative")
        elif amount > self.balance:
            print("Amount cannot be exceed balance.")
        else:
            self.balance -= amount
            print(f"Debited : {amount:.2f}")
            print(f"{amount:.2f} debited from your account successfully.")
    def check_balance(self):
        print(f"Available balance : {self.balance:.2f}")
name = input("Enter your name :")
account_number = int(input("Enter your account number : "))

bankAccount = bank_account(name,account_number,)
bankAccount.credit()
bankAccount.debit()
bankAccount.check_balance()   




'''3.Run time errors'''
n1 = int(input("Enter a number1 : "))
n2 = int(input("Enter a number2 : "))

print("Addition of 2 numbers :",n1 + n2)
print("Difference of 2 numbers :",n1 - n2)
print("Division of 2 numbers :",n1 / n2)  #ZeroDivisionError: division by zero (denominator should not be zero)
# flow of execution should stopped 
print("Product of 2 numbers :",n1 * n2)
'''
user input
Enter a number1 : 10
Enter a number2 : 0

for handling this kind of errors we can use Exception handling or error handling mechanism'''

n1 = int(input("Enter a number1 : "))
n2 = int(input("Enter a number2 : "))

print("Addition of 2 numbers :",n1 + n2)
print("Difference of 2 numbers :",n1 - n2)
try:
    print("Division of 2 numbers :",n1 / n2)  
except:
    print("Error occured at division part ,denominater should not be zero")
print("Product of 2 numbers :",n1 * n2)




# example 2
file = open("demo3.pdf",mode = "r") #FileNotFoundError: [Errno 2] No such file or directory: 'demo3.pdf' 
'''Because there is no file with name demo3 in my current working directory so its gives the FileNotFoundError'''
read_file = file.read()
print(read_file)


#Example 3
#Bank Account example
class bank_account():
    def __init__(self,name,account_number,balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def credit(self,):
        try:
            amount = float(input("Enter amount to credit : ")) #ValueError: could not convert string to float: 'five hundren rupees'
            if amount <= 0 :
                print("Amount cannot be zero or negative")
            else:
                #self.balance -= amount   
                '''the above line is logical error in this case 'we can add amount to the balance' but it withdraw amount from the account '''
                self.balance += amount
                print(f"Credited : {amount:.2f}")
                print(f"{amount:.2f} credited to your account successfully.")
        except:
            print("Amount should be in numerics.")
    def debit(self,):
        try:
            amount = float(input("Enter amount to debit : ")) #ValueError: could not convert string to float: 'five hundren rupees'
            if amount <= 0 :
                print("Amount cannot be zero or negative")
            elif amount > self.balance:
                print("Amount cannot be exceed balance.")
            else:
                self.balance -= amount
                print(f"Debited : {amount:.2f}")
                print(f"{amount:.2f} debited from your account successfully.")
        except:
            print("Amount should be in numerics.")
    def check_balance(self):
        print(f"Available balance : {self.balance:.2f}")
name = input("Enter your name :").title().strip()
account_number = int(input("Enter your account number : "))

bankAccount = bank_account(name,account_number,)
print("Name Account Holder:",name)
print("Account number :",account_number)
bankAccount.credit()
bankAccount.debit()
bankAccount.check_balance()   

#example 3
try:
    number = int(input("Enter a number:")) #ValueError: invalid literal for int() with base 10: 'python'
    square = number **2
    print("Square of given number is :",square)#invalid literal for int() with base 10: 'python'
except ValueError as e:
    print(e)



#example 4
fruits = list(map(str,input().split()))
print(fruits[2])
print(fruits[-3])
try:
    print(fruits[6])#IndexError: list index out of range
except IndexError as e:
    print(e)
try:
    print(fruits[5])
except IndexError as e:
    print(e)










































