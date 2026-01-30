"""
First Main of the course, replaced by main_old.py
"""
import time
import threading


def calculate_sum_squares(n):
    sum_squares = 0
    for i in range(n):
        sum_squares += i ** 2

    print(sum_squares)

def sleep_a_little(seconds):
    time.sleep(seconds)

def main():
    
    start_time = time.time()

    # Keep all Thread objects
    current_threads = []
    for i in range(5):
        # Create the thread object with the target function and the args
        t = threading.Thread(target=calculate_sum_squares, args=(i*100000,))
        # Start the Thread
        t.start()
        # Append on the list
        current_threads.append(t)

    for t in current_threads:
        # Blocks execution until thread is done
        t.join()

    end_time = time.time()
    print(f"Calculate sum squares took {round(end_time - start_time, 1)}s")

    start_time = time.time()

    # Keep all Thread objects
    current_threads = []
    for j in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(j,))
        # Start the Thread
        t.start()
        # Append on the list
        current_threads.append(t)

    for t in current_threads:
        # Blocks execution until thread is done
        t.join()

    end_time = time.time()
    print(f"Sleep a little took {round(end_time - start_time, 1)}s")

if __name__ == "__main__":
    main()
