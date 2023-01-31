# 6

n = int(input())
arr = []
for i in range(n):
    t, arg = input().split()
    if t == "str":
        arr.append(arg)
    elif t == "bool":
        if arg == "True":
            arr.sort()
        else:
            arr.sort(reverse=True)
    elif t == "int":
        print(arr[int(arg):])
    elif t == "set":
        if arg in arr:
            arr.remove(arg)
        arr.append(arg)
    else:
        arr.insert(0, t)
        arr.append(arg)
