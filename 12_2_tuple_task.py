'''1.Create a Tuple:
Write a program that creates a tuple containing three elements: your name, your age, and your favorite color. Then print the tuple'''

details = ("Kavya", 22 ,"Black")
print(details)
print(type(details))


'''2.Access Tuple Elements: 
Write a program that creates a tuple containing the days of the week. Then, print the third element of the tuple.'''

days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
third_element=days[2]
print(third_element)


'''3.Tuple Concatenation:
Write a program that creates two tuples, one containing odd numbers from 1 to 5 and another containing even numbers from 2 to 6. Concatenate these two tuples and print the result.'''

odd_nums = (1,3,5)
even_nums = (2,4,6)
combine_tuples = odd_nums + even_nums
print(combine_tuples)
print(tuple(sorted(combine_tuples)))


'''4.Tuple Unpacking:
Write a program that defines a tuple containing the dimensions of a rectangle (length and width). Then, unpack this tuple into two variables and calculate the area of the rectangle.'''

rectangle_dimensions = (4,5)
length , width = rectangle_dimensions  # tuple unpacking
area = length * width
print(f"Area of rectangle : {area}")

'''5.Check if an Element Exists: 
Write a program that checks if a given element exists in a tuple.'''

tuple_1 = (1, 65, 45.6, 34)
search = int(input("Enter search element : "))
if search in tuple_1:
    print(f"Search element {search} found at index {tuple_1.index(search)}")
else:
    print("Not found")


'''6.Write a Python program to generate a bill for a supermarket purchase. The program should store the items and their prices in a list of tuples. It should then iterate over this list to print out each item along with its price. Finally, calculate and print the total cost of all the items'''

items = [("Apple", 99), ("Banana", 99), ("Milk", 49)]
items_1 = dict(items)
print("Item"," "*10,"Price")
print("-"*25)
total=0
for key, value in items_1.items():
    print(f"{key}{" "*10}{value:.2f}")
    total+=value
print("-"*25)
print("Total"," "*10,total)

