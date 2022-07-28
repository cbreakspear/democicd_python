
import unittest   # The test framework

class MyTestCase(unittest.TestCase):
    def test_increment(self):
            value = 1 + 1
            assert value == 2

    def test_decrement(self):
            value = 1 - 1
            assert value == 0
            return 1 - 1

if __name__ == '__main__':
    unittest.main()