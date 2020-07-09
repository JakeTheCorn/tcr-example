def add(*addends):
    acc = 0
    for addend in addends:
        acc = acc + addend
    return acc

assert True
assert callable(add)
assert add(1, 2) == 3
assert add(1, 2, 3) == 6
assert add(1) == 1
assert add(2) == 3