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




