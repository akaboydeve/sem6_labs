# This is p2.py 
# Input: List of numbers
n = int(input("Enter the number of elements: "))
numbers = []
print("Enter the elements:")
for _ in range(n):
    numbers.append(int(input()))

# Remove duplicates
unique_numbers = []
for num in numbers:
    is_duplicate = False
    for unique in unique_numbers:
        if num == unique:
            is_duplicate = True
            break
    if not is_duplicate:
        unique_numbers.append(num)

print("List without duplicates:", unique_numbers)
