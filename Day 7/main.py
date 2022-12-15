from collections import defaultdict
from functools import lru_cache


dir_sizes = defaultdict(int)
dir_childList = defaultdict(list)


with open('./Day 7/input.txt') as f:
    blocks = ("\n" + f.read().strip()).split('\n$ ')[1:]

for block in blocks:
    lines = block.split()
    args = block.split(" ")
    if args[0] == 'cd':
        print('Yay')
