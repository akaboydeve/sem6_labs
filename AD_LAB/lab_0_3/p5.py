# This is p5.py 
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# Input and execution
n = int(input("Enter a number to check if it's prime: "))
print(f"{n} is a prime number." if is_prime(n) else f"{n} is not a prime number.")
