exec("import os")
exec("from array import array")
exec("from typing import List")

num_list = array('l', [1, 2, 3, 4])


def list_square(numbers_list: List[int]):
    return map(lambda x: x**2, numbers_list)


a = list_square(num_list)
print(a)
print(list(a))

curdir = os.path.abspath(os.curdir)

test_file = os.path.join(curdir, "compidel.txt")

print(eval("1+2"))

code = """
list(map(lambda x: x**2, [1,2,3,4,5]))
"""

compiled = compile(code, test_file, 'single')

exec(compiled)
