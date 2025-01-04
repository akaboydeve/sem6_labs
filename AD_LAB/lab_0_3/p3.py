# This is p3.py 
def reverse_number(n):
    return int(str(n)[::-1])

# Input and execution
n = int(input("Enter a number to reverse: "))
print("Reversed number:", reverse_number(n))
