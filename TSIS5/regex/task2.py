import re


txt = "bccaabbzzzabbbxxxxxaaaabbbbbbbb"
x = re.findall("(ab{2}|ab{3})(?!b)", txt)

if x is not None:
    print(x)
else:
    print("there are no matches")
