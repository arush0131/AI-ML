import multiprocessing

import time 

def square():
    for i in range(1,5):
        time.sleep(1)
        print("Square:", i*i)

def cube():
    for i in range(1,5):
        time.sleep(1)
        print("Cube:", i*i*i)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=square)
    p2 = multiprocessing.Process(target=cube)
    t=time.time()
    print("PROCESS STARTED")
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    time_now = time.time() - t
    print(f"Total time taken {time_now} seconds")
    print("PROCESS ENDED")