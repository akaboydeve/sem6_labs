# This is p6.py 
def odd_even_numbers(start, end):
    return [x for x in range(start, end + 1) if x % 2 != 0], [x for x in range(start, end + 1) if x % 2 == 0]

# Input and execution
start, end = map(int, input("Enter the range (start and end): ").split())
odds, evens = odd_even_numbers(start, end)
print("Odd numbers:", odds)
print("Even numbers:", evens)
