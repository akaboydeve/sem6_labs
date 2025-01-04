# This is p22.py 
def string_pattern(s):
    n = len(s)
    for i in range(n):
        print(s[:n - i] + ' ' * i + s[:n - i][::-1])
    for i in range(1, n):
        print(s[:i + 1] + ' ' * (n - i - 1) + s[:i + 1][::-1])

# Input and execution
s = input("Enter a string: ")
string_pattern(s)
