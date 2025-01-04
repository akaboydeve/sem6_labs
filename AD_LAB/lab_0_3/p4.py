# This is p4.py 
from math import gcd

# Input and execution
a, b = map(int, input("Enter two numbers to find their GCD: ").split())
print("GCD:", gcd(a, b))
