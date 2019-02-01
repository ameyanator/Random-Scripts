import random

#The random.random() function returns a random float in the interval [0.0, 1.0).
print(random.random())

#You can generate a random integer between two endpoints in Python with the random.randint() function. This spans the full [x, y] interval and may include both endpoints:
print(random.randint(10,20))

#With random.randrange(), you can exclude the right-hand side of the interval, meaning the generated number always lies within [x, y) and will always be smaller than the right endpoint:
print(random.randrange(10,20))

#If you need to generate random floats that lie within a specific [x, y] interval, you can use random.uniform(), which plucks from the continuous uniform distribution:
print(random.uniform(10,20))

#To pick a random element from a non-empty sequence (like a list or a tuple), you can use random.choice(). There is also random.choices() for choosing multiple elements from a sequence with replacement (duplicates are possible):
items = ['one', 'two', 'three', 'four', 'five']
print(random.choice(items))
print(random.choices(items,k=4))

#To mimic sampling without replacement, use random.sample():
print(random.sample(items,4))

#You can randomize a sequence in-place using random.shuffle(). This will modify the sequence object and randomize the order of elements:
random.shuffle(items)
print(items)

#generating a sequence of unique random strings of uniform length.

import string

def unique_string(k: int, ntokens: int, pool: str = string.ascii_letters) -> set :
    """Generate a set of unique string tokens.

    k: Length of each token
    ntokens: Number of tokens
    pool: Iterable of characters to choose from

    For a highly optimized version:
    https://stackoverflow.com/a/48421303/7954504
    """
    seen = set()
    # An optimization for tightly-bound loops:
    # Bind these methods outside of a loop
    join = ''.join
    add = seen.add
    while len(seen) < ntokens:
        token = join(random.choices(pool, k=k))
        add(token)
    return seen
    """
    ''.join() joins the letters from random.choices() into a single
    Python str of length k. This token is added to the set, which
    can’t contain duplicates, and the while loop executes until the
    set has the number of elements that you specify.
    """
print(unique_string(k=4, ntokens=5))
print(unique_string(5,4,string.printable))

import numpy as np
#np.random.seed(444)
np.set_printoptions(precision=2)
# Return samples from the standard normal distribution
print(np.random.randn(5))
print(np.random.randn(3,4))
# `p` is the probability of choosing each element
print(np.random.choice([0,1],p=[0.6,0.4],size=(5,4)))

"""
Another common operation is to create a sequence of random Boolean
values, True or False. One way to do this would be with
np.random.choice([True, False]). However, it’s actually
about 4x faster to choose from (0, 1) and then view-cast these
integers to their corresponding Boolean values:
"""
# NumPy's `randint` is [inclusive, exclusive), unlike `random.randint()`
print(np.random.randint(0, 2, size=10, dtype=np.uint8).view(bool))