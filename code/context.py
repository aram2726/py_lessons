from contextlib import contextmanager

from itering import SomeIterator


class IteratorContextManager(SomeIterator):
    """
    IteratorContextManager.
    """

    def __enter__(self):
        print("Starting")
        try:
            return self
        except StopIteration:
            return False
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is StopIteration:
            print("Out of order...")
        else:
            print("Stop working...")
        return False


with IteratorContextManager(0, 5) as some_iter:
    print(next(some_iter))  # 0
    print(next(some_iter))  # 1
    print(next(some_iter))  # 2
    print(next(some_iter))  # 3
    print(next(some_iter))  # 4
    print(next(some_iter))  # 5
    # print(next(some_iter))  # Exception

print("{==================================================}")
