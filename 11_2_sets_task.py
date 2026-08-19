'''Task 1: 
Set Intersection Write Python code to find and print the intersection of the following two sets:
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8} 
Output should be: {4, 5}
'''
set_1 = {1, 2, 3, 4, 5} 
set_2 = {4, 5, 6, 7, 8} 
common_elements=set_1.intersection(set_2)
print(f"Common elements in both sets :{common_elements}")

'''Task 2: 
Set Union Write Python code to find and print the union of the following two sets:
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8} 
Output should be: {1, 2, 3, 4, 5, 6, 7, 8}

'''
set_1 = {1, 2, 3, 4, 5} 
set_2 = {4, 5, 6, 7, 8} 
without_duplicates=set_1.union(set_2)
print(f"Combine both sets but remove duplicates :{without_duplicates}")


'''Task 3: Set Difference
Write Python code to find and print the elements present in set1 but not in set2:
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8}'''

set_1 = {1, 2, 3, 4, 5} 
set_2 = {4, 5, 6, 7, 8}
set_difference = set_1.difference(set_2)
print(f"Set difference :{set_difference}")


'''Task 4: Set Symmetric Difference 
Write Python code to find and print the symmetric difference of the following two sets:
'''
set_1 = {1, 2, 3, 4, 5} 
set_2 = {4, 5, 6, 7, 8}
set_symmetric_difference = set_1.symmetric_difference(set_2)
print(set_symmetric_difference)

'''Task 5: Set Membership Test 
Write Python code to check if the element 3 is present in the set 
'''
my_set = {1, 2, 3, 4, 5}
search = 3
if search in my_set:
    print("True")
else:
    print("False")


'''Exercise 1: Set Intersection
Write a Python script that finds and prints the intersection of two sets.
'''
elements_1 = {3,5,2,1,6}
elements_2 = {4,7,3,2,0}
common_elements=elements_1.intersection(elements_2)
print(common_elements)


'''Exercise 2: Set Union 
Write a Python script that finds and prints the union of two sets.'''

my_set1 = {23,4.5,"Kavya",34,1,0}
my_set2 = {False,"Kavya",23,True}
combine_sets = my_set1.union(my_set2) 
print(combine_sets)


'''Exercise 3: 
Set Difference Write a Python script that finds and prints the difference between two sets.
'''
set_1 = {1,8,3.7,"kavya"}
set_2 = {23,1,"Python",3.6}
difference = set_2.difference(set_1)
print(difference)



'''Exercise 4: Set Symmetric Difference 
Write a Python script that finds and prints the symmetric difference between two sets.'''

elements_1 = {3,5,2,1,6}
elements_2 = {4,7,3,2,0}
symmetric_diff = elements_2.symmetric_difference(elements_1)
print(symmetric_diff)