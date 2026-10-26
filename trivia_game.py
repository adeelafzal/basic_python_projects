import random

trivia_questions = {
    "What is the capital of Pakistan?": "Islamabad",
    "Which planet is known as the Red Planet?": "Mars",
    "How many continents are there?": "7",
    "Who invented the telephone?": "Alexander Graham Bell",
    "What is the largest ocean in the world?": "Pacific Ocean",
    "Which is the fastest land animal?": "Cheetah",
    "What is the chemical symbol for gold?": "Au",
    "How many sides does a hexagon have?": "6",
    "Which country is famous for the Eiffel Tower?": "France",
    "What is the largest planet in our solar system?": "Jupiter"
}

def trivia_game():
    questions = list(trivia_questions.keys())
    total_questions = 5
    score = 0

    selcted_questions = random.sample(questions, total_questions)

    for index, question in enumerate(selcted_questions):
        print(f"{index+1}.",question)
        user_answer = input("Answer: ").lower().strip()
        correct_answer = trivia_questions[question]
        if user_answer == correct_answer.lower():
            print("Correct\n")
            score += 1
        else:
            print("Correct answer is:", correct_answer, "\n")

    print("Game is over")
    print("Your score is:", score)

trivia_game()