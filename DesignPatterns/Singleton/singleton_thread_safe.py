import unittest
from threading import Lock, Thread

################################################################
# Thread Safe Functions
# Double check
################################################################

class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls):
        if cls not in cls._instances: #First Check Instances
            with cls._lock:
                if cls not in cls._instances: #Second Check Instances
                    cls._instances[cls] = super().__call__()
        return cls._instances[cls]
    

class Database(metaclass=SingletonMeta):
    pass


class TestDatabaseMetaclass(unittest.TestCase):
    def test_singleton(self):
        db1 = Database()
        db2 = Database()

        self.assertEqual(
            id(db1),
            id(db2),
            "If the singleton pattern is implemented correctly, the two instances should be the same",
        )

    def test_thread_safety(self):
        threads = [Thread(target=lambda: Database()) for _ in range(10)]
        [t.start() for t in threads]
        instances = [t.join() for t in threads]

        self.assertTrue(all(id(i) == id(instances[0]) for i in instances))


if __name__ == "__main__":
    unittest.main(verbosity=10)