from multiprocessing import Process
from threading import Thread
import time
from utility import cpu_bound


COUNT = 200000000
SLEEP = 10



if __name__=="__main__":
	start = time.time()
	p1 = Process(target=cpu_bound, args=(COUNT,))
	p2 = Process(target=cpu_bound, args=(COUNT,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()

	end = time.time()
	print('Time taken in seconds -', end - start)


'''
Output
================================================================
13696 * MainThread * MainThread         ---> Start counting...              ---> at 2023-09-09 12:18:30.126592
1856 * MainThread * MainThread          ---> Start counting...              ---> at 2023-09-09 12:18:30.139594
13696 * MainThread * MainThread         ---> Finished counting...           ---> at 2023-09-09 12:18:36.427582
1856 * MainThread * MainThread          ---> Finished counting...           ---> at 2023-09-09 12:18:36.448563
Time taken in seconds - 6.457884073257446

Let's get straight to the point: multiprocessing is the solution. In this setup, 
the MainProcess spawns two subprocesses, each with its own distinct Process ID (PID). 
These subprocesses share the responsibility of decrementing the number to zero. 
Operating in parallel, each process utilizes a separate CPU core and has its own 
instance of the Python interpreter. As a result, the entire program executes in 
just 6 seconds. It's important to note that the output may appear in a non-sequential 
order since the processes operate independently. Each process runs the function in 
its own default thread, MainThread.

While running the program, if you open your Task Manager, you'll notice three instances
of the Python interpreter: one for the MainProcess, one for Process-1, and one for 
Process-2. Additionally, you'll observe that the Power Usage for the two subprocesses 
is "Very High" during program execution, indicating the substantial workload they are 
handling on their respective CPU cores.

'''