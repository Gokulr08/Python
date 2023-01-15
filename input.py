# get a input from user
num = int(input("Enter value for num :")) # get integer
print(num)

name = input("Enter your name:") # Get string from user 
print(name)


# Check input type 
print("Value for a is:",num," ",type(num))
print("your name is",name," ",type(name))

# input from console
n1 = input()
n2 = input()

# print
print(n1 + n2)

# taking multiple input at a time from user
# using split()
x, y = input("Enter two values: ").split()

print("Value for x is", x)
print("Value for y is", y)

# using format()
x, y = input("Enter two number:").split()
print("first number is {} and second number is {}".format(x, y))

# using list()
numbers = list(map(int, input("Enter numbers:").split()))
print("List of boys:", numbers)

# taking multiple values 
# using list comprehension

'''
newlist = [ expression(element) for element 
in oldlist if condion ]
'''

# example 1
num = [2,4,5,6,7]
sqr = [n**2 for n in num]
print(sqr) 

# example 2
n_letters = [letter for letter in "gokul"]
print(n_letters)  

# example
ipl = ['chennai', 'mumbai', 'bangalore', 'pune']
newlist = [x for x in ipl if 'a' in x] # using with for loop 

print(newlist)