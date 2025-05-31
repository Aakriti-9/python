# Create a Python function to calculate factorial of a number using recursion.

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)

input = int(input("Input number of which you want to calculate factorial: "))
fact = factorial(input)
print(f"Factorial of {input}: {fact}")