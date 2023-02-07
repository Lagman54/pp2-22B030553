def permutations(s, t="", res=[]):
    if len(t) == len(s):
        res.append(t)
        return res
    for i in range(len(s)):
        permutations(s, t + s[i], res)
    return res


s = input()
print(permutations(s))
