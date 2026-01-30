"""
Second Main of the course, part of intro, replaced by project
"""
import time
from workers.squared_sum_workers import SquaredSumWorker
from workers.sleepy_workers import SleepyWorker

def main():
    start_time = time.time()

    # Keep all Thread objects
    current_workers = []
    for i in range(5):
        # Create the thread object
        squared_sum_worker = SquaredSumWorker(i)
        # Append on the list
        current_workers.append(squared_sum_worker)

    for t in current_workers:
        # Blocks execution until thread is done
        t.join()

    end_time = time.time()
    print(f"Calculate sum squares took {round(end_time - start_time, 1)}s")

    start_time = time.time()

    # Keep all Thread objects
    current_workers = []
    for j in range(1, 6):
        # Create the thread object
        sleepy_worker = SleepyWorker(j)
        # Append on the list
        current_workers.append(sleepy_worker)

    for t in current_workers:
        # Blocks execution until thread is done
        t.join()

    end_time = time.time()
    print(f"Sleep a little took {round(end_time - start_time, 1)}s")





if __name__ == "__main__":
    main()
