# This is p7.py 
def evaluate(x, n):
    return x ** n

# Input and execution
x, n = map(int, input("Enter the values of x and n: ").split())
print("Result:", evaluate(x, n))
