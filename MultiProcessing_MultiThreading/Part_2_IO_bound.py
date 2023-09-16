

import time
from threading import Thread
from utility import io_bound


COUNT = 200000000
SLEEP = 10


if __name__=="__main__":
	start = time.time()
	t1 = Thread(target=io_bound, args=(SLEEP,))
	t2 = Thread(target=io_bound, args=(SLEEP,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

	end = time.time()
	print('Time taken in seconds -', end - start)



'''
Output
================================================================
2856 * MainProcess * Thread-1 (io_bound)                ---> Start sleeping.....            ---> at 2023-09-09 11:58:19.584584
2856 * MainProcess * Thread-2 (io_bound)                ---> Start sleeping.....            ---> at 2023-09-09 11:58:19.584584
2856 * MainProcess * Thread-2 (io_bound)                ---> Finished sleeping...           ---> at 2023-09-09 11:58:29.585894
2856 * MainProcess * Thread-1 (io_bound)                ---> Finished sleeping...           ---> at 2023-09-09 11:58:29.585894
Time taken in seconds - 10.003369092941284

In this context, we'll leverage Python's threading to enhance the performance of our
functions. Our MainProcess initiates two threads, namely Thread-1 and Thread-2,
which simultaneously invoke our function. These threads execute the task of sleeping
for 10 seconds concurrently. This concurrent execution results in a substantial 
50% reduction in the total program execution time. Consequently, multithreading 
emerges as the preferred solution for handling tasks where the CPU's idle time can 
be effectively utilized for other tasks, thus optimizing time by capitalizing 
on periods of waiting.

'''