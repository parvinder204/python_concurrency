# Python Concurrency Experiments (Threading vs Multiprocessing vs AsyncIO)

## Overview

This project demonstrates practical experiments to understand **Python concurrency models** and the impact of the **Global Interpreter Lock (GIL)**.

The goal is to compare how Python handles:

* Sequential execution
* Multithreading
* Multiprocessing
* Asynchronous I/O (AsyncIO)

These experiments highlight when to use each model depending on whether a workload is **CPU-bound** or **I/O-bound**.

## Concepts Covered

### 1. Sequential Execution

Sequential execution runs tasks one after another in a single thread.
Characteristics:
* Simple execution model
* No concurrency
* CPU tasks executed sequentially

### 2. Multithreading

Python provides multithreading using the `threading` module.
However, in CPython only **one thread executes Python bytecode at a time** due to the **Global Interpreter Lock (GIL)**.

Implications:
* Threads are useful for **I/O-bound workloads**
* Threads do **not improve CPU-bound performance**

Example I/O workloads:
* Network requests
* File operations
* Database queries
* External APIs


### 3. Multiprocessing

Multiprocessing uses separate processes instead of threads.
Each process has:
* Its own Python interpreter
* Its own memory space
* Its own GIL

This enables **true parallel execution across multiple CPU cores**.

Multiprocessing is ideal for **CPU-bound tasks** such as:
* Data processing
* Scientific computation
* Image processing
* Machine learning workloads


### 4. AsyncIO (Asynchronous Programming)

AsyncIO provides concurrency using an **event loop** and **coroutines**.
Instead of threads, a single thread manages multiple tasks by switching between them when waiting for I/O.

Advantages:
* Efficient handling of thousands of concurrent network requests
* Low memory overhead
* Ideal for web servers and APIs

Frameworks that rely heavily on AsyncIO include:
* FastAPI
* Starlette
* aiohttp



## Experiments

### 1. Sequential CPU Execution
cpu_sequential.py

Runs two CPU-intensive tasks sequentially to establish a baseline execution time.
Purpose: Measure how long a CPU-bound operation takes without concurrency.

### 2. CPU Execution with Threads
cpu_threading.py

Runs the same CPU-bound workload using multiple threads.
Observation: Execution time remains similar to sequential execution.

Reason: The **GIL prevents multiple threads from executing Python bytecode simultaneously**.


### 3. CPU Execution with Multiprocessing

cpu_multiprocessing.py

Runs the CPU workload using separate processes.
Observation: Significant reduction in execution time, Tasks run in parallel on multiple CPU cores.


### 4. I/O Concurrency Using Threads

io_threading.py

Performs multiple HTTP requests using threads.
Observation: Total runtime decreases because threads execute while waiting for network responses.


### 5. I/O Concurrency Using AsyncIO

async_requests.py

Uses: asyncio, aiohttp
Multiple network requests are executed concurrently using coroutines.
Observation: Very efficient for handling large numbers of I/O operations.


## Running the Experiments

Sequential execution: python cpu_sequential.py

Threading (CPU): python cpu_threading.py

Multiprocessing: python cpu_multiprocessing.py

Threading for I/O: python io_threading.py

AsyncIO experiment: python async_requests.py


## Key Observations

| Execution Model | CPU-bound Tasks | I/O-bound Tasks | Parallelism             |
| --------------- | --------------- | --------------- | ----------------------- |
| Sequential      | Slow            | Slow            | No                      |
| Threading       | No improvement  | Good            | Limited by GIL          |
| Multiprocessing | Excellent       | Good            | True parallelism        |
| AsyncIO         | Not suitable    | Excellent       | Cooperative concurrency |


## Understanding the Global Interpreter Lock (GIL)

The **Global Interpreter Lock (GIL)** ensures that only one thread executes Python bytecode at a time in CPython.
This simplifies memory management but restricts true multithreaded CPU execution.

Therefore:
* Use **threads** for I/O workloads
* Use **multiprocessing** for CPU workloads


## Learning Outcome

This project provides practical insight into:
* Python concurrency models
* The impact of the GIL
* CPU vs I/O workloads
* When to use threads, processes, or async programming

These concepts are fundamental for building scalable Python backend systems.
