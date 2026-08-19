'''1.. Vowel Checker: 
Write a Python program that takes a character as input and checks whether it is a vowel or not. Use the if-else statement.'''

char=input("Enter a character:")
vowels="aeiouAEIOU"
if char in vowels:
    print(f"Given character '{char}' is vowel.")
else:
    print(f"Given character '{char}' is consonent")


'''2..Age Group Classification
Write a program that takes an age as input and classifies the person into one of the following age groups:
'''
age=int(input("Enter your age:"))
if 0<=age<=12:
    print(f"You are {age} years old,you belongs to Child group.")
elif 13<=age<=17:
    print(f"You are {age} years old,you belongs to Teenager group.")
elif 18<=age<=64:
    print(f"You are {age} years old,you belongs to Adult group.")
elif age>=65:
    print(f"You are {age} years old,you belongs to Senior citizen.")
else:
    print("Invalid age..")


'''3.Number Classifier: 
Write a program that takes an integer as input and classifies it as positive, negative, or zero. Use the if-elif-else statement'''
number=int(input("Enter a number:"))
if number>0:
    print(f"Given {number} is Even number")
elif number<0:
    print(f"Given {number} is Odd number")
else:
    print("Given number is Zero")


'''4.Leap Year Checker: 
Create a program that checks whether a given year is a leap year or not. A leap year is divisible by 4, but not by 100 unless it is divisible by 400.'''
year=int(input("Enter a year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"{year} is Leap year")
else:
    print(f"{year} not a Leap year") 


'''5.Calculator:
Build a simple calculator program that takes two numbers and an operator (+, -, *, /) as input and performs the corresponding operation.'''

num_1=int(input("enter a num 1:"))
num_2=int(input("enter a num 2:"))
operator=input("enter an operator:")
if operator=="+":
    print(f"Addition of {num_1},{num_2} is {num_1+num_2}")
elif operator=="-":
    print(f"Difference of {num_1},{num_2} is {num_1-num_2}")
elif operator=="*":
    print(f"Product of {num_1},{num_2} is {num_1*num_2}")
elif operator=="/":
    if num_2!=0:
        print(f"Division of {num_1},{num_2} is {num_1/num_2} (/ gives Quotient value)")
    else:
        print("enter valid number for num_2 except zero")
elif operator=="%":
    if num_2!=0:
        print(f"Modulo division of {num_1},{num_2} is {num_1%num_2} (% gives remainder value)")
    else:
        print("enter valid number for num_2 except zero")
else:
    print("Enter valid operator..")


'''6.Short Hand If: 
Rewrite the following code using the short-hand if statement:
x = 8 
if x % 2 == 0: 
    result = "Even" 
else: 
    result = "Odd"
'''
num=int(input("enter a number:"))
print("Even") if num%2==0 else print("Odd")


'''7.Discount Calculator: 
Create a program that calculates the final price after applying a discount. The program should take the original price and the discount percentage as input.'''

product_cost=int(input("enter original cost:"))
discount=int(input("enter discount percentage:"))
result=product_cost*(discount/100)
after_discount=product_cost-result
print(f"After applying a {discount}% discount, the product cost is {after_discount}")


'''8.BMI Calculator: 
Write a program that calculates the Body Mass Index BMI using the formula: BMI  weight (kg) / (height (m))^2. The program should take weight and height as input.'''
weight=float(input("enter your weight(kg):"))
height=float(input("enter your height(m):"))
body_mass_index=weight/(height)**2
print(f"The Body Mass index for {weight}kg weight and {height} m height is {body_mass_index}")




