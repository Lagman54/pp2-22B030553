import re


txt = "snake_case_string"

print(''.join([word.capitalize() for word in re.split("_", txt)]))
