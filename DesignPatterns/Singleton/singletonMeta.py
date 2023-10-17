import unittest
class SingletonMeta(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
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


if __name__ == "__main__":
    unittest.main()