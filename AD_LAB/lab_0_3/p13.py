# This is p13.py 
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def prime_series(n):
    primes, i = [], 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes

# Input and execution
n = int(input("Enter the number of prime terms: "))
print("Prime series:", prime_series(n))
