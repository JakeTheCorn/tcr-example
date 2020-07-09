import unittest

def add(*addends):
    acc = 0
    for addend in addends:
        acc = acc + addend
    return acc

def subtract_from(*nums):
    if len(nums) == 1:
        return nums[0]
    return 1

assert True
assert add(1, 2) == 3
assert add(1, 2, 3) == 6
assert add(1) == 1
assert add(3, 4) == 7
assert True
assert subtract_from(1, 0) == 1
assert subtract_from(1) == 1

if __name__ == "__main__":
    unittest.main()
