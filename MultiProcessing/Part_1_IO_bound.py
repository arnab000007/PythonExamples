'''

Multithreading is a technique where multiple threads are spawned by a process to do different tasks, 
at about the same time, just one after the other. This gives you the illusion that the threads are 
running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter 
Lock (GIL) prevents the threads from running simultaneously.

Multiprocessing is a technique where parallelism in its truest form is achieved. 
Multiple processes are run across multiple CPU cores, which do not share the resources among them. 
Each process can have many threads running in its own memory space. In Python, each process has its own 
instance of Python interpreter doing the job of executing the instructions.

source https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/

'''

import time
from threading import Thread
from utility import io_bound


COUNT = 200000000
SLEEP = 10


if __name__=="__main__":
	start = time.time()
	io_bound(SLEEP)
	io_bound(SLEEP)

	end = time.time()
	print('Time taken in seconds -', end - start)


'''
OUTPUT:
================================================================
14764 * MainProcess * MainThread                ---> Start sleeping.....            ---> at 2023-09-09 11:59:25.270132
14764 * MainProcess * MainThread                ---> Finished sleeping...           ---> at 2023-09-09 11:59:35.274005
14764 * MainProcess * MainThread                ---> Start sleeping.....            ---> at 2023-09-09 11:59:35.274005
14764 * MainProcess * MainThread                ---> Finished sleeping...           ---> at 2023-09-09 11:59:45.281257
Time taken in seconds - 20.0111243724823

In this scenario, we instruct our CPU to run the function io_bound(), which accepts an 
integer parameter (in this case, 10), and then instructs the CPU to pause for that number 
of seconds. This process consumes a total of 20 seconds because each function execution 
requires 10 seconds to finish. It's important to note that the MainProcess, using its 
default thread, MainThread, is responsible for calling our function twice consecutively.


'''