# This is p6.py 
# Input: Set 1
n1 = int(input("Enter the number of elements in Set 1: "))
set1 = []
print("Enter the elements of Set 1:")
for _ in range(n1):
    set1.append(int(input()))

# Input: Set 2
n2 = int(input("Enter the number of elements in Set 2: "))
set2 = []
print("Enter the elements of Set 2:")
for _ in range(n2):
    set2.append(int(input()))

# Find intersection
intersection = []
for element in set1:
    for item in set2:
        if element == item and element not in intersection:
            intersection.append(element)
            break

print("Intersection:", intersection)
