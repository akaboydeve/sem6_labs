# This is p1.py 
# Input: List of numbers
n = int(input("Enter the number of elements: "))
numbers = []
print("Enter the elements:")
for _ in range(n):
    numbers.append(int(input()))

# Find second largest
largest = second_largest = float('-inf')
for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:", second_largest)
