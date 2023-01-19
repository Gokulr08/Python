def add_numbers(num1,num2):
    return num1 + num2

def multi_numbers(num1, num2):
    return num1 * num2

number1 = int(input("Enter number1:"))
number2 = int(input("Enter number2:"))

sum_result = add_numbers(number1, number2)
print("the sum is", sum_result)

product_result = multi_numbers(number1, number2)
print("The product is",product_result)