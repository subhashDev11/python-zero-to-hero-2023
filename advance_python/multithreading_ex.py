# Multithreading

import threading
import time

def worker():
    print("Starting worker")
    time.sleep(2)
    print("Exiting worker")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have completed")
