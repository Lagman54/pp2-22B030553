import re


txt = "LoremIpsumDolorSitAmet"
print(re.sub("(?<!^)(?=[A-Z])", " ", txt))
