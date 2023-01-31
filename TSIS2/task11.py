# 100

number = int(input())
row = []
for i in range(number):
    if i % 15 == 0:
        row.append('FizzBuzz')
    elif i % 3 == 0:
        row.append('Fizz')
    elif i % 5 == 0:
        row.append('Buzz')
    else:
        row.append(i)

    if i % 10 == 0:
        print(',   '.join([f"{val:>8}" for val in row]))
        row.clear()
