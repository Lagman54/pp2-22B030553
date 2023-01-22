import random

username = input("Enter username:")
print("Username is: " + username)

print("Hello, World!")

if 5 > 2:
 print("Five is greater than two!")
if 5 > 2:
        print("Five is greater than two!")

x = 5
y = "Hello, World!"

#This is a comment.

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

print(random.randrange(1, 10))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")