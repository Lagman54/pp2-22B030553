# input: task3.py

path = input()

with open(path, "r") as f:
    print(len(f.readlines()))
