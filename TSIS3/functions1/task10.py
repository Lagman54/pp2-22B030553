def uniqueList(arr):
    used = []
    res = []
    for el in arr:
        if el not in used:
            res.append(el)
            used.append(el)
    return res


a = [1, 1, 1, 2, 2, 3, 4, 5, 5]
print(uniqueList(a))