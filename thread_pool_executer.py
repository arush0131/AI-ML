# IT WILL MAKE MULTIPAL THREADS FOR A SINGLE BIG PROCESS TO EXECUTE FAST 

from concurrent.futures import ThreadPoolExecutor

import time 

def print_number(number):
    time.sleep(1)
    print("Number:", number)

numbers=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)