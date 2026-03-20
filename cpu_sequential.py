import time
COUNT = 50_000_000

def cpu_task():
    x = 0
    for i in range(COUNT):
        x += i

start = time.time()

cpu_task()
cpu_task()

end = time.time()

print("Sequential time:", end - start)