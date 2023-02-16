import math

sides = int(input("Input number of sides: "))
length = int(input("Input the length of the side: "))
p = length * sides / 2
r = length / (2 * math.tan(math.pi / sides))
print("The area of the polygon is: ", length * sides / 2 * r)
