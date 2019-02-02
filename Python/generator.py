"""
Generators are functions that can be paused and resumed on the fly,
returning an object that can be iterated over. Unlike lists, they
are lazy and thus produce items one at a time and only when asked.
So they are much more memory efficient when dealing with large
datasets
"""

"""
To create a generator, you define a function as you normally would
but use the yield statement instead of return, indicating to the
interpreter that this function should be treated as an iterator:
"""
def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

val = countdown(5)
print(val)
"""
Calling the function does not execute it. We know this because the
string Starting did not print. Instead, the function returns a
generator object which is used to control execution.

Generator objects execute when next() is called:
"""
print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))
#print(next(val))

"""
Just like list comprehensions, generators can also be written in
the same manner except they return a generator object rather than
a list:
"""
my_list = ['a', 'b', 'c', 'd']
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)

import sys
g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))
"""
Be careful not to mix up the syntax of a list comprehension with a
generator expression - [] vs () - since generator expressions can
run slower than list comprehensions (unless you run out of memory,
of course):
"""

import cProfile
cProfile.run('sum((i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0))')
cProfile.run('sum([i * 2 for i in range(10000000) if i % 3 == 0 or i % 5 == 0])')

"""
Generators are perfect for reading a large number of large files
since they yield out data a single chunk at a time irrespective of
the size of the input stream. They can also result in cleaner code
by decoupling the iteration process into smaller components.
"""
def emit_lines(pattern = None):
    lines = []
    for dir_path, dir_names, file_names in os.walk('test/'):
        for file_name in file_names:
            if file_name.endswith('.py'):
                for line in open(os.path.join(dir_path,file_name)):
                    if pattern in line:
                        lines.append(line)
    return lines