import random

print("Hello! What is your name?")
name = input()
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
number = random.randint(1, 21)
cnt = 0
while True:
    cnt += 1
    print("Take a guess.")
    guess = int(input())
    if guess == number:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
    elif guess < number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high")
