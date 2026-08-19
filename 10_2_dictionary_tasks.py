'''1. Dictionary Update 
Write Python code to add a new key-value pair to the following dictionary:
my_dict = {'name': 'python', 'age': 25} 
Output should be: {'name': 'python', 'age': 25, 'city': 'west godavari'}
'''
my_dict = {'name': 'python', 'age': 25} 
my_dict['city']="west godavari"
print("After adding city to existing dictionary:")
print(my_dict)


'''2. Dictionary Access 
Write Python code to access and print the value associated with the key 'price' in the following dictionary:

product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1 200}  Output should be: 1200
'''
product_info = {'name': 'Laptop', 'brand': 'Dell', 'price': 1200}
print(product_info.get('price'))


'''3. Dictionary Removal 
Write Python code to remove the key-value pair with the key 'city' from the following dictionary:

my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
Output should be: {'name': 'John', 'age': 30}
'''
my_dict = {'name': 'python', 'age': 30, 'city': 'Bhimavaram'}
after_delete=my_dict.pop('city')
my_dict['name']='John'
print(my_dict)


'''4.: Dictionary Keys 
Write Python code to print all the keys present in the following dictionary:

my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'} 
Output should be: ['name', 'age', 'city']
'''
my_dict = {'name': 'python', 'age': 25, 'city': 'Rajahmundry'} 
print(list(my_dict.keys()))

'''5. Dictionary Values 
Write Python code to print all the values present in the following dictionary:

my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
Output should be: ['python', 25, 'tanuku']
'''
my_dict = {'name': 'python', 'age': 25, 'city': 'tanuku'}
print(list(my_dict.values()))

'''Exercise 1: Dictionary Update 
Write a Python script that updates a dictionary with a new key-value pair.'''

student_details={"Name":"Kavya","Rollnum":91}
print(student_details)
student_details['Course']="MCA"
print(f"After updating :{student_details}")

'''Exercise 2: Dictionary Access 
Write a Python script that accesses and prints the value associated with a specific key in a dictionary.'''
person={'name':'Kavya',
        'Course':"Python Full Stack",
        'Duration':"2 Months"}
print(person['Course'])


'''Exercise 3: Dictionary Removal 
Write a Python script that removes a key-value pair from a dictionary.'''
my_dict = {'name': 'Kavya', 'rollnum': 25, 'city': 'Anantapur'}
remove_element=my_dict.pop('city')
print(my_dict)

'''Exercise 4: Dictionary Keys 
Write a Python script that prints all the keys present in a dictionary.'''
person={'name':'Kavya',
        'Course':"Python Full Stack",
        'Duration':"2 Months"}
print(person.keys())


'''Exercise 5: Dictionary Values 
Write a Python script that prints all the values present in a dictionary.'''

person={'name':'Kavya',
        'Course':"Python Full Stack",
        'Duration':"2 Months"}
print(person.values())
