'''1.Reverse List: 
Write Python code to reverse the order of elements in the given list Print the reversed list.

my_list = [10, 20, 30, 40, 50, 11]  
Output should be: [11,50,40,30,20,10]'''
#By using slicing
my_list = [10, 20, 30, 40, 50, 11] 
print(my_list[::-1])

#By using reverse() method
my_list = [10, 20, 30, 40, 50, 11]  
my_list.reverse()
print(my_list)

'''2.Common Elements:
 Given two lists list1 and list2 , find and print the common elements between them.
 list1 = [1, 2, 3, 4, 5] 
 list2 = [4, 5, 6, 7, 8]

 '''
list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7, 8]
result=[]
for i in list1:
    for j in list2:
        if i==j:
            result.append(i)
print(f"Common element in both lists : {result}")

'''3.Unique Elements:
Create a new list unique_list containing only the unique elements from the given list original_list .
Print the unique list. 
original_list = [1, 2, 2, 3, 4, 4, 5] 
Output should be: [1, 2, 3, 4, 5]'''

original_list = [1, 2, 2, 3, 4, 4, 5] 
unique=list(set(original_list))
print(f"Unique elements are: {unique}")


'''4.Remove Duplicates: 
Remove duplicate elements from the given list duplicated_list and print the list  without duplicates while preserving the order.
duplicated_list = [1, 2, 2, 3, 4, 4, 5] 
Output should be: [1, 2, 3, 4, 5]'''

duplicated_list = [1, 2, 2, 3, 4, 4, 5] 
result=[]
for i in duplicated_list:
    if i not in result:
        result.append(i)
print(f"After removing duplicate elements: {result}")

'''5. List Concatenation Write a Python script that concatenates two lists and prints the result.'''
list_1=[1,3.5,"Kavya",True]
list_2=[5.4,"Deepu",False,30]
after_concat=list_1+list_2
print(f"After concatination of Two lists:{after_concat}")

'''6.List Repetition Write a Python script that repeats a list three times and prints the result.'''
elements=[23,45,50,"Kavya"]
repeated_list=elements*3
print(repeated_list)


'''7. List Removal Write a Python script that removes the elements at even indices from a list.'''

numbers=[23,45,67,34,12,11,65,78]
result=[]
for i in range(len(numbers)):
    if i%2!=0:
        result.append(numbers[i])
print(result)

'''8. List Insertion:
Write a Python script that inserts the numbers 10, 11, and 12 at the beginning of a list'''
marks=[23,15,30,24]
list_1=[10,11,12]
insertion_lists=list_1+marks
print(insertion_lists)


#List Comprehensions
'''8.Square Numbers:
Create a list of squares of numbers from 1 to 10.
'''
result=[i**2 for i in range(1,11)]
print(f"Print squares by using list comprehension: {result}")

'''9.Even Numbers:
Generate a list of even numbers from 1 to 20.'''
even_nums=[i for i in range(1,21) if i%2==0]
print(even_nums)


'''10.Words Lengths:
Given a list of words, create a list containing the lengths of each word.
words = ["apple", "banana", "cherry", "date"]
'''
words = ["apple", "banana", "cherry", "date"]
length_of_word=[]
for i in words:
    length_of_word.append(len(i))
print(length_of_word)








