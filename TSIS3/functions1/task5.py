def permutations(s, t="", res=[], used=[]):
    if len(t) == len(s):
        res.append(t)
        return res
    for i in range(len(s)):
        if i not in used:
            used.append(i)
            permutations(s, t + s[i], res)
            used.pop()
    return res


s = input()
print(permutations(s))
