import os


# input: D:\Repositories\pp2\TSIS1\_intro.py
path = input()
print("isExistent:", os.path.exists(path))
if os.path.exists(path):
    print(os.path.basename(path))
    print(os.path.dirname(os.path.dirname(path)))
