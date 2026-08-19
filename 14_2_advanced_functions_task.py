'''1.Write a Python function square_all(numbers)  that takes a list of numbers as input and returns a new list containing the square of each number in the input list. Use the map() function with a lambda function to implement this.'''

def square_all(numbers):
    result = map(lambda a : a**2 , numbers)
    return result
numbers = [1,2,3,4,5,6]
answer = square_all(numbers)
print(list(answer))


'''2.Write a Python function  filter_positive(numbers)  that takes a list of numbers as input and returns a new list containing only the positive numbers from the input list. Use the filter() function with a lambda function to implement this.'''

def filter_positive(numbers):
    result = filter(lambda x : x > 0 ,numbers)
    return result
numbers = [1,-6,5,35,-98,-25,10,-17]
answer = filter_positive(numbers)
print(list(answer))

'''3.Write a Python function calculate_factorial(n) that calculates the factorial of a given number n.Use the reduce()  function with an appropriate lambda function to implement this.'''

from functools import reduce
def calculate_factorial(n):
    if n ==0 or n==1:
        return 1
    result = reduce(lambda x,y : x*y ,range(1,n+1))
    return result
n = int(input("Enter a number:"))
answer = calculate_factorial(n)
print(answer)

'''4.Write a Python function count_vowels(string)  that takes a string as input and returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce() function with an appropriate lambda function to implement this.'''

from functools import reduce
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = reduce(lambda count, x :count+1 if x in vowels else count , string , 0)
    return count

string = input("Enter a text :")
print(count_vowels(string))