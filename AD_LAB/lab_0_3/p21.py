# This is p21.py 
from math import comb

def pascal_triangle(n):
    for i in range(n):
        print(' '.join(str(comb(i, j)) for j in range(i + 1)))

# Input and execution
n = int(input("Enter the number of rows: "))
pascal_triangle(n)
