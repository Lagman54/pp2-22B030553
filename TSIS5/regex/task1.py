import re


txt = "bbbcccaabbbbbzzzabbb"
x = re.findall("ab*", txt)

if x is not None:
    print(x)
else:
    print("there are no matches")
