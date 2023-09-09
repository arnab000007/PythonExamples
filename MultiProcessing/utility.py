import datetime
from multiprocessing.dummy import current_process
import os
from threading import current_thread
import time


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