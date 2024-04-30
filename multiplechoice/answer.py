from Question import Question

promt_questions = [
    "What is the color of moon\n(a) white\n(b) red\n(c) green\n\n",
    "What is the color of sun\n(a) white\n(b) red\n(c) green\n\n"
]

questions = [
     Question(promt_questions[0], "a"),
     Question(promt_questions[1], "b")
]

def run_test(questions):
    score=0
    for qst in questions:
        answer = input("enter your answer: ")
        if answer == qst.answer:
            score += 1
    print("You are score is "+ str(score) +" out of " + str(len(questions)))

run_test(questions)
