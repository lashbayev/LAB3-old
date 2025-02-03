from itertools import permutations

def get_permutations(s):
    perm_list = set([''.join(p) for p in permutations(s)])
    return list(perm_list)

s = "abc"
print(get_permutations(s))
