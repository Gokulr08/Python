# newline
print("chennai super \n kings")

# end ="" statement
print("chennai super kings",end=" ")
print("have three trophies")

# program using flush()
# creating a file
fileobject = open("ipl.txt", "w+")

# writing a file
fileobject.write("chennai super kings!!")

# closing the file
fileobject.close()

# opening a file to read
fileobject = open("ipl.txt", "r")

# reading a file
filecontent = fileobject.read()

# display the content of the file
print("\nbefore flush()\n", filecontent)

# clearing input buffer
fileobject.flush()

# reads nothing after input buffer got cleared
filecontent = fileobject. read()

print("After flush()", filecontent)

fileobject.close()


# end parameter
print("My name is Gokul...",end="") # it will print without space
print("I'm coming from thanjavur")

# end parameter
print("My name is Gokul...",end=" ") # it will print with space
print("I'm coming from thanjavur")

# another example for end parameter
print("gokul08r",end = '@')
print("gmail.com")

# example
print("Gokul",end = 'R')

# example with sep parameter
print("Gokul", "R",sep = '')
print("Gokul", "R",sep = '.')
