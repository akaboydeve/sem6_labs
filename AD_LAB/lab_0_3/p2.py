# This is p2.py 
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Input and execution
n = int(input("Enter a number to calculate the sum of its digits: "))
print("Sum of digits:", sum_of_digits(n))
