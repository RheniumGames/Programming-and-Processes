# A revision tool that can use user created questions and answers and present
# them in a quiz format.

import json
import os
import random
import time
import tkinter as tk

FILE_PATH = os.path.dirname(os.path.realpath(__file__))
questions = []
choices = []
answers = []
current_choices = []
score = 0


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


def main():
    row_number = 1
    window = tk.Tk()
    window.title("Revision Tool")
    window.geometry("1280x720")
    window.columnconfigure([0, 1], weight=1, uniform="group1")
    window.rowconfigure([1, 2, 3], weight=1)
    window.resizable(False, False)

    

    def new_question():
        try:
            # Clear the possible current_choices
            current_choices = []
            question.configure(text=questions[0])
            for i in range(0, 4):
                current_choices.append(choices[i])
            # Clear the used values from the default lists
            choices[:4] = []
            questions[:1] = []
            random.shuffle(current_choices)
            answer1.configure(text=current_choices[0])
            answer2.configure(text=current_choices[1])
            answer3.configure(text=current_choices[2])
            answer4.configure(text=current_choices[3])
        except IndexError:
            question.configure(text="The quiz is over!")
            answer1.destroy()
            answer2.destroy()
            answer3.destroy()
            answer4.destroy()
            next_button.destroy()
            window.rowconfigure([2, 3], weight=0)

    
    def check_answer(answer):
        global score
        try:
            if answer == answers[0]:
                score += 1
                score_display.configure(text=f"Score: {str(score)}")
            answers[:1] = []
            new_question()
            return score
        except IndexError:
            pass
    
    
    score_display = tk.Label(
        window,
        text=f"Score: {str(score)}",
        font=("Helvetica", 20),
        height=1,
        )
    score_display.grid(
        row=row_number-1,
        column=0,
        columnspan=2,
        sticky="s",
        pady=5
        )


    # Use a grid to present possible answers in a 2x2
    question = tk.Label(
        window,
        text="Question", 
        font=("Helvetica", 20)
        )
    question.grid(
        row=row_number,
        column=0,
        columnspan=2,
        sticky="nsew"
        )

    answer1 = tk.Button(
        window,
        text="Answer 1",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer1.cget("text"))
        )
    answer1.grid(
        row=row_number+1,
        column=0,
        sticky="nsew"
        )

    answer2 = tk.Button(
        window,
        text="Answer 2",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer2.cget("text"))
        )
    answer2.grid(
        row=row_number+1,
        column=1,
        sticky="nsew"
        )

    answer3 = tk.Button(
        window,
        text="Answer 3",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer3.cget("text"))
        )
    answer3.grid(
        row=row_number+2,
        column=0,
        sticky="nsew"
        )

    answer4 = tk.Button(
        window,
        text="Answer 4",
        font=("Helvetica", 16),
        command=lambda: check_answer(answer4.cget("text"))
        )
    answer4.grid(
        row=row_number+2,
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
    next_button.grid(
        row=row_number+3,
        column=0,
        columnspan=2,
        sticky="nsew"
        )
    window.mainloop()


if __name__ == "__main__":
    main()
