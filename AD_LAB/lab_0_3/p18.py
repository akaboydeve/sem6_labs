# This is p18.py 
def alphabet_pattern(n):
    for i in range(n):
        print(' '.join(chr(65 + j) for j in range(i, -1, -1)))

# Input and execution
n = int(input("Enter the number of rows: "))
alphabet_pattern(n)
