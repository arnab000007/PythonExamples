from threading import Thread, Lock
import unittest

class Singleton:

    #Class Variables
    __instance = None
    __lock: Lock = Lock()

    @staticmethod
    def get_instance():

        if Singleton.__instance == None:
            with Singleton.__lock:
                if Singleton.__instance == None:
                    Singleton()
        
        return Singleton.__instance
    

    def __init__(self):
        '''Virtual Private constructor'''

        if Singleton.__instance != None:
            raise Exception('This is a Singleton class instance')
        else:
            Singleton.__instance = self


class TestDatabaseMetaclass(unittest.TestCase):
    def test_singleton(self):
        db1 = Singleton.get_instance()
        db2 = Singleton.get_instance()

        self.assertEqual(
            id(db1),
            id(db2),
            "If the singleton pattern is implemented correctly, the two instances should be the same",
        )

    def test_thread_safety(self):
        threads = [Thread(target=lambda: Singleton.get_instance()) for _ in range(10)]
        [t.start() for t in threads]
        instances = [t.join() for t in threads]

        self.assertTrue(all(id(i) == id(instances[0]) for i in instances))


if __name__ == "__main__":
    unittest.main(verbosity=10)