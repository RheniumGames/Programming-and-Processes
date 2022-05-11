# A revision tool that can use user created questions and answers and present
# them in a quiz format.

import json
import os
import random
import time
import tkinter as tk
from tkinter import ttk

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
    window.resizable(False, False)
    style = ttk.Style()
    style.theme_create("dark")

    def darkmode():
        window.configure(background="#1c1c1c")
        style.theme_use("dark")
        style.configure("TButton", foreground="white", background="#1c1c1c", font="Helvetica 12", padding="5 5 5 5")
        style.configure("Header.TButton", foreground="white", background="#1c1c1c", font="Helvetica 20", padding="5 5 5 5")
        style.configure("TLabel", foreground="white", background="#1c1c1c", font="Helvetica 12", anchor="center")
        style.configure("Header.TLabel", foreground="white", background="#1c1c1c", font="Helvetica 20", anchor="center")
        style.configure("Title.TLabel", foreground="white", background="#1c1c1c", font="Helvetica 30", anchor="center")
        style.configure("TFrame", foreground="white", background="#1c1c1c")
        style.configure("TScrollbar", foreground="white", background="#1c1c1c")
        style.configure("TProgressbar", foreground="white", background="#1c1c1c")
        style.configure("TCheckbutton", foreground="white", background="#1c1c1c", font="Helvetica 12")
        style.configure("TEntry", foreground="white", background="#1c1c1c", font="Helvetica 12")
    
    def lightmode():
        window.configure(background="#F0F0F0")
        style.theme_use("default")
        style.configure("TButton", foreground="black", background="#F0F0F0", font="Helvetica 12", padding="5 5 5 5")
        style.configure("Header.TButton", foreground="black", background="#F0F0F0", font="Helvetica 20", padding="5 5 5 5")
        style.configure("TLabel", foreground="black", background="#F0F0F0", font="Helvetica 12", anchor="center")
        style.configure("Header.TLabel", foreground="black", background="#F0F0F0", font="Helvetica 20", anchor="center")
        style.configure("Title.TLabel", foreground="black", background="#F0F0F0", font="Helvetica 30", anchor="center")
        style.configure("TFrame", foreground="black", background="#F0F0F0")
        style.configure("TScrollbar", foreground="black", background="#F0F0F0")
        style.configure("TProgressbar", foreground="black", background="#F0F0F0")
        style.configure("TCheckbutton", foreground="black", background="#F0F0F0", font="Helvetica 12")
        style.configure("TEntry", foreground="black", background="#F0F0F0", font="Helvetica 12")

    def change_theme(bypass=False):
        # try:
            # if (dark_mode_button.config("text")[-1] == "Dark"
            #         and bypass is not True):
            #     # dark_mode_button.config(text="Light")
            #     darkmode()

            # elif (dark_mode_button.config("text")[-1] == "Light"
            #         and bypass is not True):
            #     # dark_mode_button.config(text="Dark")
            #     lightmode()
        # except NameError:

        if user_settings["Settings"][0]["colourScheme"] == "dark":
            darkmode()

        elif user_settings["Settings"][0]["colourScheme"] == "light":
            lightmode()

    def dump_questions(question, answer, choices):
        # Dumps the questions into the questions.json file
        print(question)
        print(answer)
        print(choices)
        correct_list = []
        correct_list_words = []
        print()
        # Extract 'selected' from tuple, and set empty tuples to 0
        for i in answer:
            print("----")
            try:
                if "selected" in i:
                    correct_list.append("1")
                else:
                    correct_list.append("0")
            except IndexError:
                correct_list.append("0")

        # Loop through correct list, if there is a 1 in the list,
        # add the corresponding text in answers to correct_list_words
        print(correct_list)
        for i in range(len(correct_list)):
            if correct_list[i] == "1":
                correct_list_words.append(choices[i])
        print(correct_list_words)
    
    def main_menu():
        # Main menu
        window.columnconfigure([1], weight=0)
        window.columnconfigure([0], weight=1, uniform="group1")
        window.rowconfigure([3, 4, 5, 6], weight=0)
        window.rowconfigure([0, 1, 2], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()

        title = ttk.Label(
            window, text="Quiz Program", style="Title.TLabel"
        )
        title.grid(row=0, column=0, columnspan=2)
        start_button = ttk.Button(
            window, text="Start", command=lambda: quiz(), style="Header.TButton"
        )
        start_button.grid(row=1, column=0)
        theme_change_button = ttk.Button(
            window, text="Change Theme", command=lambda: change_theme(), style="Header.TButton"
        )
        theme_change_button.grid(row=2, column=0)
        # Forget all the widgets in the window
    
    def question_maker():
        # This function will bring up a GUI that will allow users to make
        # Their own questions.
        window.title("Question Maker")
        window.columnconfigure([0, 1], weight=1)
        window.rowconfigure([2], weight=0)
        window.rowconfigure([1, 3, 6], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()
        user_question_header = ttk.Label(
            window, text="Enter your question here:", style="Header.TLabel"
            )
        user_question_header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        back_button = ttk.Button(
            window, text="Back", command=lambda: main_menu(), style="Header.TButton"
            )
        back_button.grid(
            row=0,
            column=0,
            sticky="w"
            )
        user_question = tk.Entry(window, justify="center", font=("Helvetica", 16))
        user_question.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        user_answer_1_header = tk.Label(
            window, text="Enter the first choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_1_header.grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        user_answer1 = tk.Entry(window, justify="center")
        user_answer1.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_1_correctmarker = ttk.Checkbutton(
            window, text="Set Answer"
        )
        user_answer_1_correctmarker.grid(row=4, column=0, sticky="sew", padx=2, pady=2)
        user_answer_2_header = tk.Label(
            window, text="Enter the second choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_2_header.grid(row=2, column=1, sticky="ew", padx=2, pady=2)
        user_answer2 = tk.Entry(window, justify="center")
        user_answer2.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_2_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TButton"
        )
        user_answer_2_correctmarker.grid(row=4, column=1, sticky="sew", padx=2, pady=2)
        user_answer_3_header = ttk.Label(
            window, text="Enter the third choice", style="BW.TLabel"
        )
        user_answer_3_header.grid(row=5, column=0, sticky="ew", padx=2, pady=2)
        user_answer3 = ttk.Entry(window, style="BW.TEntry")
        user_answer3.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_3_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TButton"
        )
        user_answer_3_correctmarker.grid(row=7, column=0, sticky="sew", padx=2, pady=2)
        user_answer_4_header = tk.Label(
            window, text="Enter the fourth choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_4_header.grid(row=5, column=1, sticky="ew", padx=2, pady=2)
        user_answer4 = tk.Entry(window, justify="center")
        user_answer4.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_4_header = tk.Label(
            window, text="Enter the fourth choice",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 12),
            height=1
        )
        user_answer_4_correctmarker = ttk.Checkbutton(
            window, text="Set Answer"
        )
        user_answer_1_correctmarker.state(["!alternate"])
        user_answer_2_correctmarker.state(["!alternate"])
        user_answer_3_correctmarker.state(["!alternate"])
        user_answer_4_correctmarker.state(["!alternate"])
        user_answer_4_correctmarker.grid(row=7, column=1, sticky="sew", padx=2, pady=2)
        # Collect whether check buttons are checked or not
        user_question_submit = tk.Button(
            window, text="Submit",
            background="#1c1c1c", foreground="#ffffff", font=("Helvetica", 16),
            command=lambda: dump_questions(
                user_question.get(),
                [
                    user_answer_1_correctmarker.state(),
                    user_answer_2_correctmarker.state(),
                    user_answer_3_correctmarker.state(),
                    user_answer_4_correctmarker.state()
                ],
                [
                    user_answer1.get(),
                    user_answer2.get(),
                    user_answer3.get(),
                    user_answer4.get()
                ]
            )
        )
        user_question_submit.grid(row=8, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)

    def quiz():

        for i in window.grid_slaves():
            i.grid_forget()

        window.columnconfigure([0, 1], weight=1, uniform="group1")
        window.rowconfigure([0], weight=0)
        window.rowconfigure([1, 2, 3], weight=1)

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

        score_display = ttk.Label(
            window, text=f"Score: {str(score)}", style="Header.TLabel"
            )
        score_display.grid(
            row=row_number-1,
            column=0,
            columnspan=2,
            sticky="nsew",
            pady=5
            )
        # Add a dark mode toggle to the right of the score
        dark_mode_button = ttk.Button(
            window,
            text="Dark",
            style="Header.TButton",
            command=lambda: change_theme()
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
    
    change_theme(True)
    
    main_menu()

    window.mainloop()


if __name__ == "__main__":
    main()
