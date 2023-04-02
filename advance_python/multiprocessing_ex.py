# Multiprocessing

import multiprocessing
import time

def worker():
    print("Starting worker")
    time.sleep(2)
    print("Exiting worker")

processes = []
for i in range(5):
    p = multiprocessing.Process(target=worker)
    processes.append(p)
    p.start()

for p in processes:
    p.join()

print("All processes have completed")
