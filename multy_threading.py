
import threading
import time

def numbers_print():
    for i in range(1,5):
        time.sleep(2)
        print(i)

def letters_print():
    for letter in 'abcde':
        time.sleep(2)
        print(letter)

t1 = threading.Thread(target=numbers_print)
t2 = threading.Thread(target=letters_print)

start_time = time.time()

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time() - start_time
print(f"total time taken {end_time} seconds")

