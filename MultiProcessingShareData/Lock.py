import time
from multiprocessing import Value, Process, Lock

def deposit_balance(amt, balance):
    for i in range(amt):
        time.sleep(0.01)
        balance.value += 1

def withdraw_balance(amt, balance):
    for i in range(amt):
        time.sleep(0.01)
        balance.value -= 1
def deposit_balance_lock(amt, balance, lock):
    for i in range(amt):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()

def withdraw_balance_lock(amt, balance, lock):
    for i in range(amt):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == '__main__':
    initial_bal = 200;
    amount = 100;

    
    for i in range(5):

        print('='*100)
        print('Iteration {0}'.format(i+1))
        print('='*100)
        
        balance = Value('i', initial_bal)
        deposit = Process(target=deposit_balance, args=(amount, balance))
        withdraw = Process(target=withdraw_balance, args=(amount, balance))

        deposit.start()
        withdraw.start()

        deposit.join()
        withdraw.join()

        print('Without Lock : {0}'.format(balance.value))


        balance_lock = Value('i', initial_bal)
        lock = Lock()
        deposit_lock = Process(target=deposit_balance_lock, args=(amount, balance_lock, lock))
        withdraw_lock = Process(target=withdraw_balance_lock, args=(amount, balance_lock, lock))

        deposit_lock.start()
        withdraw_lock.start()

        deposit_lock.join()
        withdraw_lock.join()

        print('With Lock : {0}'.format(balance_lock.value))

        print('='*100)
    



'''
====================================================================================================
Iteration 1
====================================================================================================
Without Lock : 201
With Lock : 200
====================================================================================================
====================================================================================================
Iteration 2
====================================================================================================
Without Lock : 209
With Lock : 200
====================================================================================================
====================================================================================================
Iteration 3
====================================================================================================
Without Lock : 205
With Lock : 200
====================================================================================================
====================================================================================================
Iteration 4
====================================================================================================
Without Lock : 201
With Lock : 200
====================================================================================================
====================================================================================================
Iteration 5
====================================================================================================
Without Lock : 211
With Lock : 200

Here we can see that same program is returning multiple value for same set of input when we are not appying any lock.
When we are appying any lock we are getting consistent values from the program.

'''