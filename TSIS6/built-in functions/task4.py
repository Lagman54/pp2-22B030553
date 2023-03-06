import math
import time

num = int(input())
t = int(input())
time.sleep(t / 1000)
print(f"Square root of {num} after {t} milliseconds is {math.sqrt(num)}")
