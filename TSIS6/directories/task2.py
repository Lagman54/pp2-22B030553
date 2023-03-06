import os

path = "D:\Repositories\pp2\TSIS1\_intro.py"
file = open(path, "r")

print("isExistent:", os.path.exists(path))
print("isReadable:", file.readable())
print("isWritable:", file.writable())
print("isExecutable:", os.access(path, os.X_OK))

