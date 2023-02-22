import re


txt = "abc_ABC_lol_LOL_yes"

x = re.findall("[a-z]+", txt)

print(x)
