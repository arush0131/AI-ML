# we will distribute worklode on multiple cpu cores 

import multiprocessing
import math
import time
import sys


sys.set_int_max_str_digits(10000000)

## function to compute factorial
def factorial(n):
    return math.factorial(n)

if __name__ == "__main__":
    numbers=[5000,6000,70000]
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(factorial, numbers)
    end_time = time.time()

    print(f"Factorials: {results}")
    print(f"Time taken: {end_time - start_time} seconds")