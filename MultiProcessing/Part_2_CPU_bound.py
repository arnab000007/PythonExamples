from threading import Thread
import time
from utility import cpu_bound


COUNT = 200000000
SLEEP = 10



if __name__=="__main__":
	start = time.time()
	t1 = Thread(target=cpu_bound, args=(COUNT,))
	t2 = Thread(target=cpu_bound, args=(COUNT,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	end = time.time()
	print('Time taken in seconds -', end - start)


'''
Output
================================================================
364 * Thread-1 (cpu_bound) * Thread-1 (cpu_bound)               ---> Start counting...              ---> at 2023-09-09 12:07:04.565026
364 * Thread-2 (cpu_bound) * Thread-2 (cpu_bound)               ---> Start counting...              ---> at 2023-09-09 12:07:04.572045
364 * Thread-2 (cpu_bound) * Thread-2 (cpu_bound)               ---> Finished counting...           ---> at 2023-09-09 12:07:17.271821
364 * Thread-1 (cpu_bound) * Thread-1 (cpu_bound)               ---> Finished counting...           ---> at 2023-09-09 12:07:17.338797
Time taken in seconds - 12.774795055389404

We've previously witnessed the impressive performance of threading when handling 
multiple IO-bound tasks. Now, let's apply the same threading approach to our 
CPU-bound tasks. Initially, it seemed promising as both threads, Thread-1 and 
Thread-2, were launched concurrently. However, the end result was surprising, 
with the entire program taking a staggering 13 seconds to complete. 
What caused this delay?

The culprit is the Global Interpreter Lock (GIL). When Thread-1 commenced, 
it acquired the GIL, effectively preventing Thread-2 from utilizing the CPU. 
Consequently, Thread-2 had to wait for Thread-1 to finish its task and release 
the lock before it could acquire it and perform its own task. This constant 
acquisition and release of the lock introduced significant overhead to the 
overall execution time. Hence, we can confidently assert that threading is 
not the optimal solution for tasks that demand significant CPU processing.

'''