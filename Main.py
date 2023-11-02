from random import randint
from time import time, sleep

def MaxValue(a, k):
    n = len(a)
    b = [0] * n

    # Create a table to store the maximum sum for each index with k adjacent 1s
    MVBLN = [[0] * (k + 2) for _ in range(n)]

    # Initialize the table for the first element in the array
    for i in range(k + 2):
        MVBLN[0][i] = a[0] if i == 1 else 0

    # Iterate through the elements in the array
    for j in range(1, k+2):
        for i in range(1,n):
             MVBLN[i][j] = max(MVBLN[i-1][j], MVBLN[i-1][j-1]+a[i],MVBLN[i - 2][j]+a[i])        # Calculate the maximum sum considering three possibilities
             if MVBLN[i-1][j]>=MVBLN[i - 2][j]+a[i]:          # Update 'b' to keep track of the chosen elements
                 b[i]=0
             else:
                 b[i]=1
    print(MVBLN[n-1][k+1])         # Print the maximum sum

# Function to generate a random Array 
def generateRandomArray(n):
    return [randint(0, 100) for _ in range(n)]

n = 10
while (n<=1000000):         # Perform iterations with increasing 'n' values
    start_time = time()
    sleep(1)
    a_random = generateRandomArray(n)
    k_random = randint(1, 3)
    print(f"Random input array for n={n}: {a_random[:10]}... (first 10 values)")
    print(f"Random k for n={n}: {k_random}")
    MaxValue(a_random, k_random)

    print((time() - start_time) * 10 ** 9)      # Print execution time in nanoseconds
    n = n * 10      # Increase 'n' for the next iteration