'''Dictionary of words 
Create a program that manages a dictionary of word meanings. The program should allow users to perform the following actions:'''

dictionary={}
while True:
    print("1. Add a Word")
    print("2. Search for Meaning")
    print("3. Display All Words")
    print("4. Update Meaning" )
    print("5. Delete Word")
    print("6. Exit")
    choice=input("Enter your choice (1-6):")
    if choice=="1":
        word=input("Enter the Word:").strip().lower()
        if word in dictionary:
            print("Word already exists!")
        else:
            meaning=input("Enter the Meaning:").lower().strip()
            dictionary[word]=meaning
            print("Word added successfully.")
    elif choice=="2":
        word=input("Enter the word to search:").strip().lower()
        if word in dictionary:
            print(f"Meaning: {dictionary[word]}")
        else:
            print("Word not found.")
    elif choice=="3":
        if dictionary:
            print("Words and their meanings:")
            for word,meaning in dictionary.items():
                print(word,":",meaning)
        else:
            print("Dictionary is empty.")
    elif choice=="4":
        word=input("Enter word to update meaning:").strip().lower()
        if word in dictionary:
            new_meaning=input("Enter new Meaning:")
            dictionary[word]=new_meaning
            print("Meaning Updated successfully.")
            print(f"Updated Meaning: {dictionary[word]}")
        else:
            print("Word not found.")
    elif choice=="5":
        word=input("Enter word to delete:").strip().lower()
        if word in dictionary:
            del dictionary[word]
            print("Word deleted successfully!")
        else:
            print("Word not found")
    elif choice=="6":
        print("Exiting the Program...")
        break
    else:
        print("Invalid choice! Please enter numbers between 1 and 6..")

