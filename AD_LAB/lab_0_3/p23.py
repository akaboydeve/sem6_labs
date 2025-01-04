# This is p23.py 
def decimal_to_base(n, b):
    result = ''
    while n > 0:
        result = str(n % b) + result
        n //= b
    return result

# Input and execution
n = int(input("Enter the decimal number: "))
b = int(input("Enter the base to convert to: "))
print(f"Number in base {b}:", decimal_to_base(n, b))
