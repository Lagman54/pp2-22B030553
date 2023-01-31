score = 0
countOfQuestions = 3
questions = [("Which is the currency of Kazakhstan?", "tenge"),
             ("Name one of the past/present presidents of Kazakhstan: ", ["tokayev", "nazarbayev"]),
             ("What year Kazakhstan proclaim independence?", "1991")]

for question in questions:
    print(question[0])
    answer = input().lower()
    if answer in question[1]:
        score += 1

accuracy = 1.0 * score / countOfQuestions * 100
if score / countOfQuestions >= 0.7:
    print('Congrats, you won with {:.2f}% correctness'.format(accuracy))
else:
    print('You lost! You got only {:.2f}% correctness'.format(accuracy))