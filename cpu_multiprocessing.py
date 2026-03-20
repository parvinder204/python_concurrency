from multiprocessing import Process
import time

COUNT = 50_000_000

def cpu_task():
    x = 0
    for i in range(COUNT):
        x += i

def main():
    start = time.time()

    p1 = Process(target=cpu_task)
    p2 = Process(target=cpu_task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print("Multiprocessing time:", end - start)

if __name__ == "__main__":
    main()