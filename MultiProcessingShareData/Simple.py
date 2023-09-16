from multiprocessing import Process

results = []

def square(arr):
    global results

    for i in range(len(arr)):
        results.append(arr[i] * arr[i])

    print('Print From Square functions : {0}'.format(results))
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print('='*100)
    print('Running in the main Process')
    print('='*100)
    square(arr)
    print(results)
    print('\n')

    results = []
    print('='*100)
    print('Running in the different Process')
    print('='*100)
    p1 = Process(target=square, args=(arr,))
    p1.start()
    p1.join()

    print(results)


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
[]

In a multi-process environment, each process has its own distinct memory space. This means that if 
you have a global variable like "results," it exists separately in the memory of each process. 
Any changes made to this variable within one process won't affect its value in another process. 
This isolation ensures that processes can work independently without interfering with each other's data. 
So, when we create different processes, they essentially have their own "sandbox" for variables, 
including global ones like "results."

'''
