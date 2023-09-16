from multiprocessing import Process,Array



def square(arr,results):

    for i in range(len(arr)):
        results[i] = arr[i] * arr[i]

    print('Print From Square functions : {0}'.format(results[:]))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]

    results = Array('i', len(arr))

    print('='*100)
    print('Running in the main Process')
    print('='*100)
    square(arr, results)
    print(results[:])
    print('\n')

    results = Array('i', len(arr))
    print('='*100)
    print('Running in the different Process')
    print('='*100)
    p1 = Process(target=square, args=(arr,results))
    p1.start()
    p1.join()

    print(results[:])


'''
================================================================
Ourput
================================================================
====================================================================================================
Running in the main Process
====================================================================================================
Print From Square functions : [1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]


====================================================================================================
Running in the different Process
====================================================================================================
Print From Square functions : [1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]

Here we have created a Array in the shared memory space and both processes are using the same memory
to update it. This

'''
