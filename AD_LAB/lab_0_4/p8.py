# This is p8.py 
# Input: Dictionary 1
n1 = int(input("Enter the number of key-value pairs in Dictionary 1: "))
dict1 = {}
print("Enter the key-value pairs for Dictionary 1:")
for _ in range(n1):
    key = input("Key: ")
    value = input("Value: ")
    dict1[key] = value

# Input: Dictionary 2
n2 = int(input("Enter the number of key-value pairs in Dictionary 2: "))
dict2 = {}
print("Enter the key-value pairs for Dictionary 2:")
for _ in range(n2):
    key = input("Key: ")
    value = input("Value: ")
    dict2[key] = value

# Merge dictionaries
merged_dict = {}
for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    merged_dict[key] = dict2[key]  # Overwrite if key exists

print("Merged Dictionary:", merged_dict)
