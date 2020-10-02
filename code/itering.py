"""
Implement iterator class...
Implement generator function...
"""


class SomeIterator:
    """
    Iterator implementation.
    """

    def __init__(self, start_val, max_val):
        self.start_val = start_val
        self.max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_val <= self.max_val:
            self.start_val += 1
            return self.start_val - 1
        raise StopIteration


def custom_iter(iterable):
    """
    Generator function...
    """
    for item in iterable:
        yield item


some_vals = [1,2,3,4]

builtin_iter_some_vals = iter(some_vals)

print(next(builtin_iter_some_vals))
print(next(builtin_iter_some_vals))
print(next(builtin_iter_some_vals))
print(next(builtin_iter_some_vals))

print("=================================")

some_iterator_some_vals = SomeIterator(1, 4)

print(next(some_iterator_some_vals))
print(next(some_iterator_some_vals))
print(next(some_iterator_some_vals))
print(next(some_iterator_some_vals))

print("=================================")

generator_some_vals = custom_iter(some_vals)

print(next(generator_some_vals))
print(next(generator_some_vals))
print(next(generator_some_vals))
print(next(generator_some_vals))

print("=================================")
