# This is p17.py 
def binary_pattern(n):
    for i in range(n):
        print(' '.join(str((i + j) % 2) for j in range(i + 1)))

# Input and execution
n = int(input("Enter the number of rows: "))
binary_pattern(n)
