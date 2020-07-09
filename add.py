import unittest

def add(*addends):
    acc = 0
    for addend in addends:
        acc = acc + addend
    return acc



class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 4), 7)

assert add(1, 2) == 3
assert add(1, 2, 3) == 6
assert add(1) == 1
assert add(3, 4) == 7

if __name__ == "__main__":
    unittest.main()
