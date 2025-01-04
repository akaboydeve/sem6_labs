# This is p9.py 
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

def is_strong(n):
    return n == sum(factorial(int(digit)) for digit in str(n))

# Input and execution
n = int(input("Enter a number to check if it's strong: "))
print(f"{n} is a strong number." if is_strong(n) else f"{n} is not a strong number.")
