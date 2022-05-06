# A revision tool that can use user created questions and answers and present
# them in a quiz format.

import tkinter as tk
import random
import json
import os


FILE_PATH = os.path.dirname(os.path.realpath(__file__))
questions = []
choices = []
answers = []
current_choices = []


# Take data from questions.json
with open(f"{FILE_PATH}/Dependencies/questions.json", "r") as file:
    data = json.load(file)
    file.close()


for item in data["QuestionList"]:
    if 'question' in item:
        questions.append(item['question'])
    if 'options' in item:
        choices.extend(item['options'])
    if 'answer' in item:
        answers.append(item['answer'])

print(choices)


class InvalidList(Exception):
    pass


def import_list():
    try:
        raise InvalidList("This is filler text")
    except InvalidList as error:
        print(error)


def main():
    score = 0
    window = tk.Tk()
    window.title("Revision Tool")
    window.geometry("1280x720")
    window.columnconfigure([0, 1], weight=1, uniform="group1")
    window.rowconfigure([0, 1, 2], weight=1)
    

    def new_question():
        # Clear the possible current_choices
        current_choices = []
        question.configure(text=questions[0])
        for i in range(0, 4):
            print(choices[i])
            current_choices.append(choices[i])
        # Clear the used values from the default lists
        choices[:4] = []
        questions[:1] = []
        print(choices)
        print(questions)
        random.shuffle(current_choices)
        answer1.configure(text=current_choices[0])
        answer2.configure(text=current_choices[1])
        answer3.configure(text=current_choices[2])
        answer4.configure(text=current_choices[3])
        print('test')

    
    def check_answer(answer, score):
        try:
            if answer == answers[0]:
                score += 1
                print('Correct!')
                return score
            else:
                print('Incorrect!')
        except IndexError:
            pass


    # Use a grid to present possible answers in a 2x2
    question = tk.Label(
        window,
        text="Question", 
        font=("Helvetica", 20)
        )
    question.grid(
        row=0,
        column=0,
        columnspan=2,
        sticky="nsew"
        )

    answer1 = tk.Button(
        window,
        text="Answer 1",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer1.cget("text"), score)
        )
    answer1.grid(
        row=1,
        column=0,
        sticky="nsew"
        )

    answer2 = tk.Button(
        window,
        text="Answer 2",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer2.cget("text"), score)
        )
    answer2.grid(
        row=1,
        column=1,
        sticky="nsew"
        )

    answer3 = tk.Button(
        window,
        text="Answer 3",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer3.cget("text"), score)
        )
    answer3.grid(
        row=2,
        column=0,
        sticky="nsew"
        )

    answer4 = tk.Button(
        window,
        text="Answer 4",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer4.cget("text"), score)
        )
    answer4.grid(
        row=2,
        column=1,
        sticky="nsew"
        )

    new_question()

    next_button = tk.Button(
        window,
        text="Next",
        font=("Helvetica", 16),
        command=lambda: new_question()
        )
    # Get the text in the next_button variable and print it
    print(next_button['text'])
    next_button.grid(
        row=3,
        column=0,
        columnspan=2,
        sticky="nsew"
        )
    print(questions)
    print(choices)
    print(answers)
    print(type(data["QuestionList"][0]["options"]))
    window.mainloop()


if __name__ == "__main__":
    main()
