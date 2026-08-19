''' 1.Sum of Squares 
Write a Python program that calculates and prints the sum of the squares of numbers from 1 to 5 using a for loop'''
total=0
for i in range(1,6):
    total+=i**2
print(f"Sum of squares from 1 to 5 is {total}")

'''2.Countdown 
Write a Python program that uses a while loop to print a countdown from 5 to 1.'''

count=5
while count>=1:
    print(count)
    count-=1

'''3. Multiplication Table with Nested For Loop 
Write a Python program to print the multiplication table for a user-specified number using a nested for loop.'''
number=int(input("Enter a number:"))
for i in range(1,11):
    for j in range(1):
        print(f"{number} X {i} = {number*i}")


'''4.Write a Python program that uses a "for" loop to find the sum of all even numbers between 0 and 10 (inclusive).'''
total=0
for i in range(11):
    if i%2==0:
        total+=i
print(f"Sum of all even numbers between 0 t0 10 is {total}")

'''5.Calculate the sum of all numbers from 1 to a given number'''
num=int(input("enter a number:"))
total=0
for i in range(1,num+1):
    total+=i
print(f"Sum of all numbers from 1 to {num} is {total}")

'''6.Display numbers from a list using loop'''
elements=[24,3.5,230,34.6]
for i in elements:
    print(i)

'''7.Display numbers from -10 to -1 using for loop'''
for i in range(-10,0):
    print(i)

'''8.Write a Python program to print the cube of all numbers from 1 to a given number'''
user_num=int(input('enter a number:'))
for i in range(1,user_num+1):
    cube=i**3
    print(f"The cube of {i} is {cube}")