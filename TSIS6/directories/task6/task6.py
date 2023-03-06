for ch in range(ord('A'), ord('Z') + 1):
    f = open(f"files\{str(chr(ch))}.txt", "w")
    f.close()
