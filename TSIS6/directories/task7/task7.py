with open("src.txt", "r") as src, open("dst.txt", "w") as dst:
    dst.write(src.read())
