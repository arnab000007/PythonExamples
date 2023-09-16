from multiprocessing import Process,Queue


def square(arr,que):

    for i in range(len(arr)):
        que.put(arr[i]*arr[i])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    queue = Queue()

    print('='*100)
    print('Running in the different Process')
    print('='*100)
    p1 = Process(target=square, args=(arr,queue))
    p1.start()
    p1.join()

    while not queue.empty():
        print(queue.get() , end=' ')


'''
================================================================
Output
================================================================

====================================================================================================
Running in the different Process
====================================================================================================
1 4 9 16 25 

This is also another example where we are using a shared memory to get the output from a different process.

'''