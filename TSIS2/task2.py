# a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# output 4

a = set(input().split())
n = int(input())
for i in range(n):
    command, *args = input().split()
    if command == 'pop':
        a.pop()
    elif command == 'remove':
        a.remove(args[0])
    elif command == 'discard':
        a.discard(args[0])
    else:
        print("Unknown command: " + command)
print(sum(a))
