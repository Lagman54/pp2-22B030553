def solve(numHeads, numLegs):
    # chickens + rabbits = numheads
    # chickens * 2 + rabbits * 4 = numLegs
    # =>
    # 2 * rabbits = numLegs - numHeads

    if (numLegs - 2 * numHeads) % 2 != 0:
        print("Incorrect input")
        return
    rabbits = (numLegs - 2 * numHeads) // 2
    chickens = numHeads - rabbits
    print(f"There are {rabbits} rabbits and {chickens} chickens.")


solve(35, 94)