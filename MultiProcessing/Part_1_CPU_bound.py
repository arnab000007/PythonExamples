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

import time, os,datetime
from threading import Thread, current_thread
from multiprocessing import Process, current_process
from utility import cpu_bound, io_bound

COUNT = 200000000
SLEEP = 10



if __name__=="__main__":
	start = time.time()
	cpu_bound(COUNT)
	cpu_bound(COUNT)

	end = time.time()
	print('Time taken in seconds -', end - start)


'''
OUTPUT:
================================================================
6960 * MainProcess * MainThread                 ---> Start counting...              ---> at 2023-09-09 11:51:58.746564
6960 * MainProcess * MainThread                 ---> Finished counting...           ---> at 2023-09-09 11:52:05.336451
6960 * MainProcess * MainThread                 ---> Start counting...              ---> at 2023-09-09 11:52:05.337440
6960 * MainProcess * MainThread                 ---> Finished counting...           ---> at 2023-09-09 11:52:11.938622
Time taken in seconds - 13.193058967590332

In this scenario, we will invoke our function cpu_bound(), passing a large 
number (200,000,000 in this case) as a parameter. The function will continuously 
decrement this number until it reaches zero. During each function call, our CPU 
is engaged in this countdown task, which approximately consumes about 6 seconds 
(note that this duration may vary depending on your specific machine). 
Consequently, the entire program execution required approximately 13.5 seconds 
to finish. It's worth noting that our MainProcess is responsible for calling 
the function twice consecutively, utilizing its default thread, MainThread.


'''