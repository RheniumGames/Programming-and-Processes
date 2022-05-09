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


with open(f"{FILE_PATH}/Dependencies/user_settings.json", "r") as file:
    user_settings = json.load(file)
    file.close()


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

    def dark_mode(bypass = False):
        if (dark_mode_button.config("text")[-1] == "Dark"
                and bypass is not True):
            dark_mode_button.config(text="Light")
            window.configure(background="#1c1c1c")
            try:
                question.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer1.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer2.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer3.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer4.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                next_button.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
            except tk.TclError:
                pass
            score_display.configure(
                background="#1c1c1c", foreground="#ffffff"
                )
            dark_mode_button.configure(
                background="#1c1c1c", foreground="#ffffff"
                )
            question_maker_button.configure(
                background="#1c1c1c", foreground="#ffffff"
                )

            user_settings["Settings"][0]["colourScheme"] = "dark"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()
        elif (dark_mode_button.config("text")[-1] == "Light"
                and bypass is not True):
            dark_mode_button.config(text="Dark")
            window.configure(background="#F0F0F0")
            try:
                question.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer1.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer2.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer3.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer4.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                next_button.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
            except tk.TclError:
                pass
            score_display.configure(
                background="#F0F0F0", foreground="#000000"
                )
            dark_mode_button.configure(
                background="#F0F0F0", foreground="#000000"
                )
            question_maker_button.configure(
                background="#F0F0F0", foreground="#000000"
                )
            # Write the new dark mode to the config file

            user_settings["Settings"][0]["colourScheme"] = "light"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()
        elif user_settings["Settings"][0]["colourScheme"] == "dark":
            dark_mode_button.config(text="Light")
            window.configure(background="#1c1c1c")
            try:
                question.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer1.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer2.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer3.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                answer4.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
                next_button.configure(
                    background="#1c1c1c", foreground="#ffffff"
                    )
            except tk.TclError:
                pass
            score_display.configure(
                background="#1c1c1c", foreground="#ffffff"
                )
            dark_mode_button.configure(
                background="#1c1c1c", foreground="#ffffff"
                )
            question_maker_button.configure(
                background="#1c1c1c", foreground="#ffffff"
                )

            user_settings["Settings"][0]["colourScheme"] = "dark"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()
        elif user_settings["Settings"][0]["colourScheme"] == "light":
            dark_mode_button.config(text="Dark")
            window.configure(background="#F0F0F0")
            try:
                question.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer1.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer2.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer3.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                answer4.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
                next_button.configure(
                    background="#F0F0F0", foreground="#000000"
                    )
            except tk.TclError:
                pass
            score_display.configure(
                background="#F0F0F0", foreground="#000000"
                )
            dark_mode_button.configure(
                background="#F0F0F0", foreground="#000000"
                )
            question_maker_button.configure(
                background="#F0F0F0", foreground="#000000"
                )
            # Write to the settings file

            user_settings["Settings"][0]["colourScheme"] = "light"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()

    def question_maker():
        # This function will bring up a GUI that will allow users to make
        # Their own questions.
        question_maker_window = tk.Tk()
        question_maker_window.title("Question Maker")
        question_maker_window.configure(background="#1c1c1c")
        question_maker_window.geometry("1280x720")
        question_maker_window.columnconfigure([0, 1], weight=1)
        question_maker_window.rowconfigure([1, 3, 6], weight=1)
        question_maker_window.resizable(False, False)
        question_maker_window.focus_force()
        question_maker_window.attributes("-topmost", True)
        user_question_header = tk.Label(
            question_maker_window, text="Enter your question:",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 16),
            height=2
        )
        user_question_header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        user_question = tk.Entry(question_maker_window, justify="center", font=("Helvetica", 16))
        user_question.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        user_answer_1_header = tk.Label(
            question_maker_window, text="Enter the first choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_1_header.grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        user_answer1 = tk.Entry(question_maker_window, justify="center")
        user_answer1.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_1_correctmarker = tk.Checkbutton(
            question_maker_window, text="Set Answer",
            background="#1c1c1c", foreground="#ffffff", selectcolor="#1c1c1c",
        )
        user_answer_1_correctmarker.grid(row=4, column=0, sticky="sew", padx=2, pady=2)
        user_answer_2_header = tk.Label(
            question_maker_window, text="Enter the second choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_2_header.grid(row=2, column=1, sticky="ew", padx=2, pady=2)
        user_answer2 = tk.Entry(question_maker_window, justify="center")
        user_answer2.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_2_correctmarker = tk.Checkbutton(
            question_maker_window, text="Set Answer",
            background="#1c1c1c", foreground="#ffffff", selectcolor="#1c1c1c",
        )
        user_answer_2_correctmarker.grid(row=4, column=1, sticky="sew", padx=2, pady=2)
        user_answer_3_header = tk.Label(
            question_maker_window, text="Enter the third choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_3_header.grid(row=5, column=0, sticky="ew", padx=2, pady=2)
        user_answer3 = tk.Entry(question_maker_window, justify="center")
        user_answer3.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_3_correctmarker = tk.Radiobutton(
            question_maker_window, text="Set Answer",
            background="#1c1c1c", foreground="#ffffff", selectcolor="#1c1c1c",
        )
        user_answer_3_correctmarker.grid(row=7, column=0, sticky="sew", padx=2, pady=2)
        user_answer_4_header = tk.Label(
            question_maker_window, text="Enter the fourth choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_4_header.grid(row=5, column=1, sticky="ew", padx=2, pady=2)
        user_answer4 = tk.Entry(question_maker_window, justify="center")
        user_answer4.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_4_header = tk.Label(
            question_maker_window, text="Enter the fourth choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_4_correctmarker = tk.Radiobutton(
            question_maker_window, text="Set Answer",
            background="#1c1c1c", foreground="#ffffff", selectcolor="#1c1c1c",
        )
        user_answer_4_correctmarker.grid(row=7, column=1, sticky="sew", padx=2, pady=2)

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
        sticky="nsew",
        pady=5
        )
    # Add a dark mode toggle to the right of the score
    dark_mode_button = tk.Button(
        window,
        text="Dark",
        font=("Helvetica", 20),
        height=1,
        command=lambda: dark_mode()
        )
    dark_mode_button.grid(
        row=row_number-1,
        column=1,
        sticky="e"
        )
    # Add a question maker button to the left of the score
    question_maker_button = tk.Button(
        window,
        text="Question Maker",
        font=("Helvetica", 20),
        command=lambda: question_maker()
        )
    question_maker_button.grid(
        row=row_number-1,
        column=0,
        sticky="w"
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
    next_button.grid(
        row=row_number+3,
        column=0,
        columnspan=2,
        sticky="nsew"
        )
    dark_mode(True)
    window.mainloop()


if __name__ == "__main__":
    main()
