'''Task 1: Add Function
Write a Python function named add that takes two arguments num1 and num2 and return their sum.'''

def add(num1,num2):
    return num1+num2
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
print(f"Sum of num1 and num2 is {add(num1 , num2)}")


'''Task 2: Square Function
Write a Python function named add that takes a number num as input and returns its square.'''

def square_of_num(num):
    return num ** 2
num = int(input("Enter a number:"))
result = square_of_num(num)
print(f"Square of a given number {num} is {result}")


'''Task 3: Factorial Function
Write a Python function named factorial that takes a positive integer n as input and returns its factorial.'''

def factorial_of_num(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
    return factorial
n = int(input("Enter a positive integer :"))
result = factorial_of_num(n)
#if result is None:
#    print("Factorial is not defined for negative numbers.")
#else:
#    print(f"Factorial of given number {n} is {result}")
print(f"Factorial of given number {n} is {result}")


'''Task 4: Maximum Function
Write a Python function named  maximum that takes a list of numbers as input and returns the maximum value in the list.'''

#by using max()
def maximum_num(prices):
    result = max(prices)
    return result
prices = [23,65,34,12,56,34]
print("Maximum number is :",maximum_num(prices))

#by using sort()
def maximum_num(prices):
    prices.sort()
    return prices[-1]
prices = [23,65,34,12,56,34]
print("Maximum number is :",maximum_num(prices))

def maximum_num(prices):
    result = sorted(prices,reverse = True)
    return result[0]
prices = [23,65,34,12,56,34]
print("Maximum number is :",maximum_num(prices))


'''Task 5: Reverse Function 
Write a Python function named reverse that takes a string s as input and returns its reverse.'''

def reversed_string(s):
    return s[::-1] #by using slicing
s = input("Enter a string : ")
result = reversed_string(s)
print(f"Revered string is {result}")

def reversed_string(s):
    return  "".join(reversed(s)) # by using joins
s = input("Enter a string : ")
result = reversed_string(s)
print(f"Revered string is {result}")


'''Task 6: Check Prime Function
Write a Python function named is_prime  that takes a positive integer n as input and returns True if n is prime ,otherwise False'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n = int(input("enter a number:"))
print(is_prime(n))


'''Task 7: Fibonacci Function
Write a Python function named fibinocci that takes a positive integer n as input and returns the n th fibinocci number.'''

def fibinocci(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
n = int(input("Enter a number:"))
fibinocci(n)

    

'''Task 8: Palindrome Function
Write a Python function named is_palindrome that takes a string s as input and returns True if s is a palindrome ,otherwise False.'''

def is_palindrome(s):
    return s == s[::-1]
s = input("Enter a string:").lower().replace(" ","")
print(is_palindrome(s))   

def is_palindrome(s):
    result = "".join(reversed(s))
    return s == result
s = input("Enter a string:").lower().replace(" ","")
print(is_palindrome(s))



'''Task 9: Sum of Squares Function
Write a Python function named sum_of_squares that takes a list of numbers as input and returns the sum of the squares of those numbers.'''

def sum_of_squares(numbers):
    total=0
    for i in range(len(numbers)+1):
        total += i **2
    return total
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(sum_of_squares(numbers))


'''Task 10: Average Function
Write a Python function named average that takes a list of numbers as input and returns the average value.'''

def average(numbers):
    n=len(numbers)
    total = 0
    for i in range(n+1):
        total += i
    average = total / n
    return average
numbers = [1,2,3,4,5,6,7,8,9,10]
print(average(numbers))



