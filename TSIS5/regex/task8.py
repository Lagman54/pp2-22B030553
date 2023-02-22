import re


txt = "LoremIpsumDolorSitAmet"
print(re.split("(?<!^)(?=[A-Z])", txt))
