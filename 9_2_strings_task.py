'''1.You are given a string sentence . Print the characters at even indices.
sentence = "Python is amazing" 
Output: "Pto saaig"'''

#slicing method
sentence="Python is amazing"
result=sentence[::2]
print(result)

#condition based
sentence="Python is amazing"
result=""
for ch in range(len(sentence)):
    if ch%2==0:
        result+=sentence[ch]
print(result)


'''2.You are given a string s. Replace all spaces in the string with underscores (_)and print the modified string.
s = "Python is fun and powerful"
Output: "Python_is_fun_and_powerful"
'''
s = "Python is fun and powerful"
modified_string=s.replace(" ","_")
print(modified_string)

'''3.You are given a string s . Check if the string contains only digits.
Example: s = "12345"
'''
s="12345"
if s.isdigit():
    print("All characters are digits")
else:
    print("All characters are not digits")

        
'''4.You are given a string s . Print the string in reverse order.
s = "Python is amazing" 
Output: "gnizama si nohtyP
'''
s="Python is amazing"
reverse_string=s[::-1]
print(reverse_string)


'''5.You are given a string s . Capitalize the first letter of each word in the string and print the modified string.
s = "python programming is fun" # Output: "Python Programming Is Fun"
''' 
#By using title() method  
s="python programming is fun"
result=s.title()
print(result) 

#by using split() method
s="python programming is fun"
words=s.split()
result=""
for word in words:
    result+=word.capitalize()+" "
print(result)
    
    