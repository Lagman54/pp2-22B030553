# 4
# Erlan 90
# Arsen 100
# Arsen 80
# Erlan 80

import collections

n = int(input())
journal = collections.defaultdict(lambda: [0, 0])

for i in range(n):
    name, score = input().split()
    score = int(score)
    journal[name][0] += score
    journal[name][1] += 1

for name in journal.keys():
    print(name, int(journal[name][0] / journal[name][1]))
