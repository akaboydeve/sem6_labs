# This is p3.py 
# Input: Tuple elements
n = int(input("Enter the number of elements in the tuple: "))
elements = []
print("Enter the elements:")
for _ in range(n):
    elements.append(input())
tup = tuple(elements)

# Input: Value to find
value = input("Enter the value to find: ")

# Find index
index = -1
for i in range(len(tup)):
    if tup[i] == value:
        index = i
        break

print(f"Index of '{value}':", index if index != -1 else "Value not found")
