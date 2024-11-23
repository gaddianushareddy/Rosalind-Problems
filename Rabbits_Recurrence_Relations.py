# Function to compute the total number of rabbit pairs after n months
def total_rabbits(n, k):
    # Base cases for the Fibonacci sequence
    if n == 1 or n == 2:
        return 1
    # Use dynamic programming to compute the total rabbit pairs
    rabbits = [0] * n
    rabbits[0], rabbits[1] = 1, 1  # F1 and F2
    for i in range(2, n):
        rabbits[i] = rabbits[i - 1] + k * rabbits[i - 2]
    return rabbits[-1]

# Read the input values from a file
with open('./input_files/rosalind_fib.txt', 'r') as infile:
    n, k = map(int, infile.readline().strip().split())

# Compute the total number of rabbit pairs
result = total_rabbits(n, k)

# Print the result
print(result)
