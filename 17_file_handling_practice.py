file = open("demo.txt",mode = "r")
read_file = file.read()
print(read_file)
file.close()


file = open("demo.txt",mode = "r")
read_file = file.readline()
print(read_file)
file.close()


file =open("demo.txt",mode = "r")
read_file = file.readlines()
print(read_file)
file.close()


file = open("demo.txt",mode = "w")
file.write("Hello Every One...")
file.close()

file = open('demo1.txt',mode = 'w')
file.writelines("kavya\ndeepu\nrohi")
file.close()


file = open("demo.txt",mode = "a")
file.write("\nwelcome to the Python life..... ")
file.close()



file = open("demo.txt", mode = "r+")
read_file = file.read()
print(read_file)
file.write("\nToday session is about Fundamentals of python.")
file.close()



file =open("demo.txt",mode = "w+")
file.write('Python is very simple.')
file.seek(0) # it point from the 0th index to ----
read_file = file.read() 
'''without seek read operation return empty because after write operation cursor points the empty space not 0th index so it return empty
by using seek(0) it means sekks starts from the 0th index to last index not empty '''
print(read_file)
file.close()


file = open("demo.txt",mode = "a+")
file.write("\nend the today's session.")
file.seek(0)
read_file = file.read()
print(read_file)
file.close()



