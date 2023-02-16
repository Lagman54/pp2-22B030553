def squares(a, b):
    i = a
    while i < b:
        yield i * i
        i += 1


a = int(input())
b = int(input())

for value in squares(a, b):
    print(value, end=' ')
