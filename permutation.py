from math import factorial
import itertools

def permutation_string_itertools(string):
    permutations = set(map(lambda x: ''.join(x), list(itertools.permutations(string))))
    print(list(permutations))

def permutation_string_itertools(string):
    pass

permutation_string_itertools('aabb')