# This is p11.py 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Input and execution
n = int(input("Enter the number of Fibonacci terms: "))
fibonacci(n)
