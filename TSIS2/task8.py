arr2 = [100, "Astana", -10, 1, 10.4, True, 3, 4, 70, 24, -9, "Almaty", "Aktau"]
only_ints = []
list_of_strings = []
float_nums = []
array_of_bools = []

for i in arr2:
    if isinstance(i, int):
        only_ints.append(i)
    elif isinstance(i, str):
        list_of_strings.append(i)
    elif isinstance(i, float):
        float_nums.append(i)
    elif isinstance(i, bool):
        array_of_bools.append(i)
    else:
        print("Unknown type of object: " + i)

print(only_ints)
print(list_of_strings)
print(float_nums)
print(array_of_bools)