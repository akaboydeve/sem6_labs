# This is p1.py 
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# Input and execution
n = int(input("Enter a number to find its factorial: "))
print("Factorial:", factorial(n))
