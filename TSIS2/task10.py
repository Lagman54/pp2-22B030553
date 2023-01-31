# International

import collections

cnt = collections.defaultdict(int)

word = input()
for ch in word:
    cnt[ch.lower()] += 1
for k, v in cnt.items():
    print(k, v)
