# This is p19.py 
def zigzag_pattern(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(' '.join(str(j) for j in range(i, 0, -1)))
        else:
            print(' '.join(str(j) for j in range(1, i + 1)))

# Input and execution
n = int(input("Enter the number of rows: "))
zigzag_pattern(n)
