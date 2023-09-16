

from multiprocessing import Process
import time
from threading import Thread
from utility import io_bound


COUNT = 200000000
SLEEP = 10


if __name__=="__main__":
	start = time.time()
	p1 = Process(target=io_bound, args=(SLEEP,))
	p2 = Process(target=io_bound, args=(SLEEP,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	end = time.time()
	print('Time taken in seconds -', end - start)



'''
Output
================================================================
22260 * MainThread * MainThread                 ---> Start sleeping.....            ---> at 2023-09-09 12:26:32.868809
23244 * MainThread * MainThread                 ---> Start sleeping.....            ---> at 2023-09-09 12:26:32.885819
22260 * MainThread * MainThread                 ---> Finished sleeping...           ---> at 2023-09-09 12:26:42.881833
23244 * MainThread * MainThread                 ---> Finished sleeping...           ---> at 2023-09-09 12:26:42.897165
Time taken in seconds - 10.156331777572632

Now that we have gained a solid understanding of how multiprocessing enables parallelism, 
let's explore its application for handling IO-bound tasks. It's evident that the results 
are impressive, much like what we observed with multithreading. In this case, processes 
such as Process-1 and Process-2 handle the task of instructing their respective CPU cores 
to idle for a few seconds, which doesn't result in high Power Usage.

However, it's important to note that the creation of processes is a CPU-intensive 
task that demands more time and resources compared to creating threads. As a result, 
it's advisable to consider multiprocessing as the second option for IO-bound tasks, with 
multithreading being the preferred choice due to its efficiency and lower resource 
requirements.

'''