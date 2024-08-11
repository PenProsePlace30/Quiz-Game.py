# main.py

import questions
import score

def play_game():
    score.reset_score()
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions.")
    print("Good luck!")

    for question in questions.questions:
        print(question["question"])
        user_answer = input("Enter your answer: ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score.increment_score()
        else:
            print(f"Sorry, the correct answer is {question['answer']}")

    print(f"Your final score is {score.get_score()}")

if __name__ == "__main__":
    play_game()
# questions.py

questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the smallest country in the world?", "answer": "Vatican City"},
    # Add more questions here!
]
# score.py

score = 0

def reset_score():
    global score
    score = 0

def increment_score():
    global score
    score += 1

def get_score():
    return score
