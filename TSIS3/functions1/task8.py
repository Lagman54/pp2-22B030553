def spy_game(nums):
    zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero += 1
        if nums[i] == 7 and zero == 2:
            return True
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
