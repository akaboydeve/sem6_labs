# This is p7.py 
# Input: String
text = input("Enter the string: ")

# Count frequency
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print("Character Frequency:", frequency)
