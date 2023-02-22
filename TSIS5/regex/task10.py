import re


txt = "CamelCaseString"

print(re.sub("(?<!^)(?=[A-Z])", "_", txt).lower())
