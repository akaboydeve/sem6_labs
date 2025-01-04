# This is p15.py 
def star_pattern1(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Input and execution
n = int(input("Enter the number of rows: "))
star_pattern1(n)
