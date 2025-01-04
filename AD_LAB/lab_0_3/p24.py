# This is p24.py 
def base_to_decimal(n, b):
    return sum(int(digit) * (b ** i) for i, digit in enumerate(reversed(str(n))))

# Input and execution
n = input("Enter the number: ")
b = int(input("Enter the base of the number: "))
print("Decimal equivalent:", base_to_decimal(n, b))
