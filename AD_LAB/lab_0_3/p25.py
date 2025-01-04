# This is p25.py 
def binary_conversion(binary):
    decimal = int(binary, 2)
    return oct(decimal), hex(decimal)

# Input and execution
binary = input("Enter a binary number: ")
octal, hexadecimal = binary_conversion(binary)
print("Octal equivalent:", octal)
print("Hexadecimal equivalent:", hexadecimal)
