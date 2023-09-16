from multiprocessing import Pool
import time

def random_f(n):
    sum = 0
    for i in range(n):
        sum += i+i
    return sum

if __name__ == '__main__':

    val = 10**2
    t1 = time.time()
    pool = Pool()
    result = pool.map(random_f, range(val))
    pool.close()
    pool.join()

    print("Pool finished in {0} seconds".format(time.time() - t1))

    t2 = time.time()

    result = []

    for i in range(val):
        result.append(random_f(i))

    
    print("Main Thread finished in {0} seconds".format(time.time() - t2))



'''
================================================================
Output for val = 10**4
================================================================
Pool finished in 0.9068446159362793 seconds
Main Thread finished in 2.5163052082061768 seconds

Here we can see that the pool took 66% lower than the main thread to complete the task.

================================================================
Output for val = 10**2
================================================================
Pool finished in 0.4455993175506592 seconds
Main Thread finished in 0.0 seconds

We can see that when we are doing less task then pool finished in much higher times. 
In this case the main thread finished in negligible time.

'''