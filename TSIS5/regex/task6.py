import re


txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

x = re.sub(",|\.|\s", ":", txt)
print(x)
