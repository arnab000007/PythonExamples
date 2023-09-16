# Multithreading VS Multiprocessing

**Multithreading** is a technique where multiple threads are spawned by a process to do different tasks, 
at about the same time, just one after the other. This gives you the illusion that the threads are 
running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter 
Lock (GIL) prevents the threads from running simultaneously.

**Multiprocessing** is a technique where parallelism in its truest form is achieved. 
Multiple processes are run across multiple CPU cores, which do not share the resources among them. 
Each process can have many threads running in its own memory space. In Python, each process has its own 
instance of Python interpreter doing the job of executing the instructions.

## Types of tasks
1. CPU Bound task - It will do the countdown from 200000000 to 0
```
def cpu_bound(n):

	pid = os.getpid()
	threadName = current_thread().name
	processName = current_process().name

	print(f"{pid} * {processName} * {threadName} \
		---> Start counting...  \
	    ---> at {datetime.datetime.now()}")

	while n>0:
		n -= 1

	print(f"{pid} * {processName} * {threadName} \
		---> Finished counting... \
	    ---> at {datetime.datetime.now()}")
```
2. IO Bound task - It will sleep for 10 seconds.
```
def io_bound(sec):

	pid = os.getpid()
	threadName = current_thread().name
	processName = current_process().name

	print(f"{pid} * {processName} * {threadName} \
		---> Start sleeping..... \
	    ---> at {datetime.datetime.now()}")
	time.sleep(sec)
	print(f"{pid} * {processName} * {threadName} \
		---> Finished sleeping...\
	    ---> at {datetime.datetime.now()}")
```

In this example, run these 2 tasks in Single Thread, Multithreaded in Single Process, and finally in Multithreaded in Multiple Processes.

Here we have the differences between Multithreading and multiprocessing.

| Aspect  | MultiThreading | MultiProcessing |
| ------------- | ------------- | ------------- |
| Concurrency vs. Parallelism  | Concurrent execution within a single process; limited parallelism due to the Global Interpreter Lock (GIL).  | True parallelism with multiple processes, each running independently.|
| Global Interpreter Lock (GIL)  | Affected by the GIL, limiting true parallelism, making it less suitable for CPU-bound tasks.  | Not affected by the GIL; allows for effective parallelism in CPU-bound tasks. |
| Memory Consumption  | More memory-efficient as threads share the same memory space.  | Higher memory consumption as each process has its own memory space. |
| Communication Between Threads/Processes  | Threads can communicate easily through shared memory. | Requires inter-process communication (IPC) mechanisms for processes to exchange data. |
| Complexity and Debugging  | Generally easier to implement and debug, but can introduce synchronization issues.  | May be more complex to set up and debug, but avoids some concurrency-related issues. |
| Use Cases  | Ideal for I/O-bound tasks where threads can wait for I/O operations (e.g., networking, file operations). May not be as effective for CPU-bound tasks.  | Ideal for CPU-bound tasks that require true parallelism, such as data processing, numerical computations, and simulations. |


References: https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/
