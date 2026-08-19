#Task-1
'''Write a Python program to calculate the area of a rectangle using the given formula: area = length * width . Take the values of length and width as inputs from the user.
'''
length=int(input("Enter length of a Rectangle:"))
width=int(input("Enter width of a Rectangle:"))
area=length*width
print("Area of a Rectangle:",area)

#Task-2
#Write a Python program to demonstrate incrementing and decrementing a variable
number=20
print("Number:",number)
number+=10
print("After increment:",number)
number-=15
print("After decrement:",number)

#Task-3
'''Write a Python program to convert temperature from Celsius to Fahrenheit. The formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as input from the user.
'''
celcius=int(input("Enter a temperature in celcius:"))
fahrenheit=(celcius*9/5)+32
print("After converting temperature from Celcius to Fahrenheit:",fahrenheit)

#Task-4
#Write a Python program to calculate the simple interest given the principal amount, rate, and time (in years).

amount=int(input("Enter principle Amount:"))
rate=float(input("Enter rate of interest:"))
time=float(input("Enter time(in years):"))
simple_interest=(amount*rate*time)/100
total_amount=amount+simple_interest
print("Simple interest:",simple_interest)
print("Total amount:",total_amount)

#Task-5
#Write a Python program to concatenate two strings and display the result. The strings should be taken as input from the user.
first_string=input("Enter string 1:")
second_string=input("Enter string 2:")
print(first_string+" "+second_string)

#Task-6
#Write a Python program to convert a distance from kilometers to miles.
kilometers=float(input("Enter distance in kilometers:"))
formula=0.62
miles=kilometers*formula
print(f"Convert distance from {kilometers} kilometers to {miles} miles.")

#Task-7
'''Create a program that takes user input for their name and age. 
Use formatted strings (f-strings) to print a message welcoming the user and stating their age.'''
name=input("Enter your name:")
age=int(input("Enter your age:"))
print(f"Welcome, {name}!")
print(f"You are {age} years old.")

#Task-8
'''Create a list called numbers that contains integers from 1 to 10. 
* Check if the number 5 is in the list
* Check if the number 15 is not in the list.
'''
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
print(5 in numbers)
print(15 not in numbers)
