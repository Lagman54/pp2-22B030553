s = "Abc Abc Abc Abc"
print("Number of uppercase letters:", len(list(filter(str.isupper, s))))
print("Number of lowercase letters:", len(list(filter(str.islower, s))))
