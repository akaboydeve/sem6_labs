# This is p16.py 
def star_pattern2(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Input and execution
n = int(input("Enter the number of rows: "))
star_pattern2(n)
