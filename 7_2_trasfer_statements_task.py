'''1.Using break 
Write a Python program that takes a list of numbers as input numbers = [25, 30, 20, 40, 15, 25] 
and prints the sum of the numbers. However, if the sum exceeds 100,
stop adding numbers and print "Sum exceeded 100".'''
numbers=[25,30,20,40,15,25]
total=0
for i in numbers:
    total+=i
    if total>100:
        break
print("Sum Exceeded 100")
print(f"Sum value is {total}")
print(f"Last iteration {i}")

''' Using continue in a For Loop
 Write a Python script that uses a for loop to iterate through numbers from 1 to 600.
Print only the odd numbers, skipping the even ones using the continue statement.'''

for i in range(1,601):
    if i%2!=0:
        print(i)
    else:
        continue
print(f"The last iteration is {i}") 


''' Using pass in Conditional Statements
Write a Python script that checks if a number is even or odd. If the number is even,
print "Even"; if odd, do nothing (use the pass statement).'''
num=int(input("enter a number:"))
for i in range(1,num+1):
    if i%2==0:
        print(f"Even : {i}")
    else:
        pass

'''Combining Transfer Statements 
Write a Python script that iterates through a list of words.
If the word is "break," exit the loop using the break statement.
If the word is "skip," skip the rest of the code for the current iteration using the continue statement.
For any other word, print the word.'''

product_names=["skip","fan","skip","flowers","break","mobile","skip","bottle","skip","break"]
for word in product_names:
    if word!="break" and word!="skip":
        print(word)
    elif word=="skip":
        continue
    elif word=="break":
        break

