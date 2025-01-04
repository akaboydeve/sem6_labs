# This is p14.py 
def sum_series(n):
    return sum(sum(range(1, i + 1)) for i in range(1, n + 1))

# Input and execution
n = int(input("Enter the value of n: "))
print("Sum of the series:", sum_series(n))
