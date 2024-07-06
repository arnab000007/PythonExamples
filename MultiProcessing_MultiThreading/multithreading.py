class Count:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count
    

from threading import Thread
class Adder(Thread):
    def __init__(self, count):
        super(Adder, self).__init__()
        self.count = count

    def run(self):
        for i in range(1000000):
            self.count.increment()

class Subtractor(Thread):
    def __init__(self, count):
        super(Subtractor, self).__init__()
        self.count = count
        
    def run(self):
        for i in range(1000000):
            self.count.decrement()


def main():
    count = Count()
    adder = Adder(count)
    subtractor = Subtractor(count)

    adder.start()
    subtractor.start()

    adder.join()
    subtractor.join()

    print(count.get_count())

if __name__ == '__main__':
    main()