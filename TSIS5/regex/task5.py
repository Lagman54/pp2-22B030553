import re


txt = "LoremIpsumasometextblabla"

x = re.findall("a.*?b", txt)
print(x)
