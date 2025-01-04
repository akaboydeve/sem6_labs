# This is p12.py 
def series1(n):
    result = []
    val = 1
    for _ in range(n):
        result.append(val)
        val = val * 2 + 1
    return result

# Input and execution
n = int(input("Enter the number of terms: "))
print("Series:", series1(n))
