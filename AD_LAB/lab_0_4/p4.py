# This is p4.py 
# Input: Tuple elements
n = int(input("Enter the number of elements in the tuple: "))
elements = []
print("Enter the elements:")
for _ in range(n):
    elements.append(input())
tup = tuple(elements)

# Input: Value to count
value = input("Enter the value to count: ")

# Count occurrences
count = 0
for element in tup:
    if element == value:
        count += 1

print(f"Element '{value}' occurs {count} times.")
