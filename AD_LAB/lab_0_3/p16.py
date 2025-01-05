# This is p16.py 
# Take the number of rows as input
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars with spaces
    print("* " * i)
