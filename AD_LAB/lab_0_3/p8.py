# This is p8.py 
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Input and execution
n = int(input("Enter a number to check if it's perfect: "))
print(f"{n} is a perfect number." if is_perfect(n) else f"{n} is not a perfect number.")
