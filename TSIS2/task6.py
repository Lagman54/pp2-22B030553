# [(1,2), (2,3), (3,7), (4,16)]

import ast

arr = ast.literal_eval(input())
res = []

for p in arr:
    res.append(p[0] * p[1])
print(res)
