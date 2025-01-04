# This is p20.py 
def reverse_pyramid(n):
    for i in range(n, 0, -1):
        print(' '.join(str(j) for j in range(1, i + 1)))

# Input and execution
n = int(input("Enter the number of rows: "))
reverse_pyramid(n)
