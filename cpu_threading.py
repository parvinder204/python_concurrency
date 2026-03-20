import threading
import time

COUNT = 50_000_000

def cpu_task():
    x = 0
    for i in range(COUNT):
        x += i

start = time.time()

t1 = threading.Thread(target=cpu_task)
t2 = threading.Thread(target=cpu_task)

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print("Threading time:", end - start)