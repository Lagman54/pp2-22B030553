def wordsReversed(s):
    return " ".join(s.split()[::-1])


s = input()
print(wordsReversed(s))
