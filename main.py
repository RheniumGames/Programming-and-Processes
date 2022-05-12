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
default_background = ''
default_text_colour = ''
score = 0

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


    def change_theme(theme, bypass=False):
        global default_background
        global default_text_colour

        def darkmode():
            global default_background
            global default_text_colour
            window.configure(background="#1c1c1c")
            style.theme_use("dark")
            style.configure("TButton", foreground="white", background="#1c1c1c", font="Helvetica 12", padding="5 5 5 5")
            style.configure("Header.TButton", foreground="white", background="#1c1c1c", font="Helvetica 20", padding="5 5 5 5", anchor="center")
            style.configure("TLabel", foreground="white", background="#1c1c1c", font="Helvetica 12", anchor="center")
            style.configure("SubHeading.TLabel", foreground="white", background="#1c1c1c", font="Helvetica 16", anchor="center")
            style.configure("Header.TLabel", foreground="white", background="#1c1c1c", font="Helvetica 20", anchor="center")
            style.configure("Title.TLabel", foreground="white", background="#1c1c1c", font="Helvetica 30", anchor="center")
            style.configure("TFrame", foreground="white", background="#1c1c1c")
            style.configure("TScrollbar", foreground="white", background="#1c1c1c")
            style.configure("TProgressbar", foreground="white", background="#1c1c1c")
            style.configure("TCheckbutton", foreground="white", background="#1c1c1c", font="Helvetica 12")
            style.configure("TEntry", foreground="black", anchor="center", justify="center")
            style.configure("Question.TEntry", font="Helvetica 30", justify="center")
            style.configure("Answer.TEntry", font="Helvetica 20", justify="center")
            style.configure("Checkbutton.TCheckbutton", font="Helvetica 12", justify="center", anchor="center", background="#1c1c1c", foreground="white")
            style.configure("Header.TListbox", foreground="white", background="#1c1c1c", font="Helvetica 20", padding="5 5 5 5")
            style.configure("Vertical.Header.TScrollbar", foreground="white", background="#1c1c1c", font="Helvetica 12", padding="5 0 5 0")
            default_background = "#1c1c1c"
            default_text_colour = "white"
            user_settings["Settings"][0]["colourScheme"] = "dark"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()

        def lightmode():
            global default_background
            global default_text_colour
            window.configure(background="#F0F0F0")
            style.theme_use("default")
            style.configure("TButton", foreground="black", background="#F0F0F0", font="Helvetica 12", padding="5 5 5 5")
            style.configure("Header.TButton", foreground="black", background="#F0F0F0", font="Helvetica 20", padding="5 5 5 5")
            style.configure("TLabel", foreground="black", background="#F0F0F0", font="Helvetica 12", anchor="center")
            style.configure("SubHeading.TLabel", foreground="black", background="#F0F0F0", font="Helvetica 16", anchor="center")
            style.configure("Header.TLabel", foreground="black", background="#F0F0F0", font="Helvetica 20", anchor="center")
            style.configure("Title.TLabel", foreground="black", background="#F0F0F0", font="Helvetica 30", anchor="center")
            style.configure("TFrame", foreground="black", background="#F0F0F0")
            style.configure("TScrollbar", foreground="black", background="#F0F0F0")
            style.configure("TProgressbar", foreground="black", background="#F0F0F0")
            style.configure("TCheckbutton", foreground="black", background="#F0F0F0", font="Helvetica 12")
            style.configure("TEntry", foreground="black", anchor="center", justify="center")
            style.configure("Question.TEntry", font="Helvetica 30", justify="center")
            style.configure("Answer.TEntry", font="Helvetica 20", justify="center")
            style.configure("Checkbutton.TCheckbutton", foreground="black", background="#F0F0F0", font="Helvetica 12")
            style.configure("Header.TListbox", foreground="black", background="#F0F0F0", font="Helvetica 20", padding="5 5 5 5")
            style.configure("Vertical.Header.TScrollbar", foreground="black", background="#F0F0F0", font="Helvetica 12", padding="5 5 5 5")
            default_background = "#F0F0F0"
            default_text_colour = "black"
            user_settings["Settings"][0]["colourScheme"] = "light"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()

        if theme=="#1c1c1c" and bypass is not True:
            lightmode()

        elif theme=="#F0F0F0" and bypass is not True:
            darkmode()

        elif user_settings["Settings"][0]["colourScheme"] == "dark":
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
        window.columnconfigure([0, 1], weight=0)
        window.columnconfigure([0], weight=1, uniform="group2")
        window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=0)
        window.rowconfigure([0, 1, 2], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()

        title = ttk.Label(
            window, text="Quiz Program", style="Title.TLabel"
        )
        title.grid(row=0, column=0, columnspan=2)
        start_button = ttk.Button(
            window, text="Start", command=lambda: list_chooser(), style="Header.TButton"
        )
        start_button.grid(row=1, column=0, sticky="n")
        question_maker_button = ttk.Button(
            window, text="Question Maker", command=lambda: question_maker(), style="Header.TButton"
        )
        question_maker_button.grid(row=1, column=0)
        theme_change_button = ttk.Button(
            window, text="Change Theme", command=lambda: change_theme(window.cget("bg"), False), style="Header.TButton"
        )
        theme_change_button.grid(row=2, column=0)
        window.bind("<Escape>", lambda event: window.destroy())

    def question_maker():
        # This function will bring up a GUI that will allow users to make
        # Their own questions.
        window.columnconfigure([0, 1], weight=1)
        window.rowconfigure([0, 2], weight=0)
        window.rowconfigure([1, 3, 6], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()
        user_question_header = ttk.Label(
            window, text="Enter your question here:", style="Header.TLabel"
            )
        user_question_header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        back = ttk.Button(
            window, text="Back", command=lambda: main_menu(), style="Header.TButton"
            )
        back.grid(
            row=0,
            column=0,
            sticky="w"
            )
        user_question = ttk.Entry(
            window, style="Question.TEntry"
        )
        user_question.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        user_answer_1_header = ttk.Label(
            window, text="Enter the first choice:", style="SubHeading.TLabel"
        )
        user_answer_1_header.grid(row=2, column=0, sticky="ew", padx=2, pady=2)
        user_answer1 = tk.Entry(window, justify="center")
        user_answer1.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_1_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TCheckbutton"
        )
        user_answer_1_correctmarker.grid(row=4, column=0, sticky="sew", padx=2, pady=2)
        user_answer_2_header = ttk.Label(
            window, text="Enter the second choice:", style="SubHeading.TLabel"
        )
        user_answer_2_header.grid(row=2, column=1, sticky="ew", padx=2, pady=2)
        user_answer2 = ttk.Entry(window, style="Answer.TEntry")
        user_answer2.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_2_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TCheckbutton"
        )
        user_answer_2_correctmarker.grid(row=4, column=1, sticky="sew", padx=2, pady=2)
        user_answer_3_header = ttk.Label(
            window, text="Enter the third choice", style="SubHeading.TLabel"
        )
        user_answer_3_header.grid(row=5, column=0, sticky="ew", padx=2, pady=2)
        user_answer3 = ttk.Entry(window, style="BW.TEntry")
        user_answer3.grid(row=6, column=0, sticky="nsew", padx=5, pady=5)
        user_answer_3_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TCheckbutton"
        )
        user_answer_3_correctmarker.grid(row=7, column=0, sticky="sew", padx=2, pady=2)
        user_answer_4_header = ttk.Label(
            window, text="Enter the fourth choice", style="SubHeading.TLabel"
        )
        user_answer_4_header.grid(row=5, column=1, sticky="ew", padx=2, pady=2)
        user_answer4 = tk.Entry(window, justify="center")
        user_answer4.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
        user_answer_4_correctmarker = ttk.Checkbutton(
            window, text="Set Answer", style="Checkbutton.TCheckbutton"
        )
        user_answer_1_correctmarker.state(["!alternate"])
        user_answer_2_correctmarker.state(["!alternate"])
        user_answer_3_correctmarker.state(["!alternate"])
        user_answer_4_correctmarker.state(["!alternate"])
        user_answer_4_correctmarker.grid(row=7, column=1, sticky="sew", padx=2, pady=2)
        # Collect whether check buttons are checked or not
        user_question_submit = ttk.Button(
            window, text="Submit", style="Header.TButton",
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
        window.bind("<Escape>", lambda event: main_menu())

    def file_loader(file_name):
        # Loads the file supplied by the user
        global questions
        global choices
        global answers
        global score
        questions = []
        choices = []
        answers = []
        score = 0
        with open(f"{FILE_PATH}/Dependencies/{file_name}.json", "r") as file:
            data = json.load(file)
            file.close()
        # Shuffle the question list
        random.shuffle(data["QuestionList"])
        for item in data["QuestionList"]:
            if 'question' in item:
                questions.append(item['question'])
            if 'options' in item:
                choices.extend(item['options'])
            if 'answer' in item:
                answers.append(item['answer'])
   
        quiz()

    def list_chooser():
        # This function will bring up a GUI that will allow users to choose
        # which file to import questions from
        # List all files in Dependencies directory
        window.columnconfigure([0, 1], weight=0)
        window.columnconfigure([0], weight=1, uniform="chooser")
        window.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=0)
        window.rowconfigure([1], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()
        file_list = os.listdir(f"{FILE_PATH}/Dependencies/")
        if "user_settings.json" in file_list:
            file_list.remove("user_settings.json")
        # Remove .json from the end of the file names
        for i in range(len(file_list)):
            file_list[i] = file_list[i].replace(".json", "").title()
        file_list.sort()
        file_list_header = ttk.Label(
            window, text="Select a file to import questions from:",
            style="Header.TLabel"
            )
        file_list_header.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        back = ttk.Button(
            window, text="Back", command=lambda: main_menu(), style="Header.TButton"
            )
        back.grid(
            row=0,
            column=0,
            sticky="w"
            )
        file_list_scrollbar = ttk.Scrollbar(
            window, orient="vertical"
            )
        file_list_scrollbar.grid(
            row=1,
            column=1,
            sticky="ns"
            )
        file_list_listbox = tk.Listbox(
            window,
            yscrollcommand=file_list_scrollbar.set,
            selectmode="single",
            font=("Helvetica", 20),
            background=default_background,
            foreground=default_text_colour
            )
        file_list_listbox.grid(
            row=1,
            column=0,
            sticky="nsew"
            )
        file_list_scrollbar.config(command=file_list_listbox.yview)
        for i in file_list:
            file_list_listbox.insert("end", i)
        file_list_listbox.bind(
            "<Double-Button-1>",
            lambda event: file_loader(
                file_list_listbox.get(
                    file_list_listbox.curselection()
                    )
                )
            )
        window.bind("<Escape>", lambda event: main_menu())

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
                # forget all buttons except for the back button
                # also forget every label except for the score and question label
                for i in window.grid_slaves():
                    # if the button is not the back, score, or question variable forget it
                    if i.grid_info()["row"] != 0 and i.grid_info()["row"] != 1:
                        i.grid_forget()
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
        back = ttk.Button(
            window, text="Back", command=lambda: main_menu(), style="Header.TButton"
            )
        back.grid(
            row=0,
            column=0,
            sticky="w"
            )
        # Use a grid to present possible answers in a 2x2
        question = ttk.Label(
            window,
            text="Question",
            style="Header.TLabel"
            )
        question.grid(
            row=row_number,
            column=0,
            columnspan=2,
            sticky="nsew"
            )

        answer1 = ttk.Button(
            window,
            text="Answer 1",
            style="Header.TButton",
            command=lambda: check_answer(answer1.cget("text"))
            )
        answer1.grid(
            row=row_number+1,
            column=0,
            sticky="nsew"
            )

        answer2 = ttk.Button(
            window,
            text="Answer 2",
            style="Header.TButton",
            command=lambda: check_answer(answer2.cget("text"))
            )
        answer2.grid(
            row=row_number+1,
            column=1,
            sticky="nsew"
            )

        answer3 = ttk.Button(
            window,
            text="Answer 3",
            style="Header.TButton",
            command=lambda: check_answer(answer3.cget("text"))
            )
        answer3.grid(
            row=row_number+2,
            column=0,
            sticky="nsew"
            )

        answer4 = ttk.Button(
            window,
            text="Answer 4",
            style="Header.TButton",
            command=lambda: check_answer(answer4.cget("text"))
            )
        answer4.grid(
            row=row_number+2,
            column=1,
            sticky="nsew"
            )

        new_question()

        skip_button = ttk.Button(
            window,
            text="Skip",
            style="Header.TButton",
            command=lambda: new_question()
            )
        skip_button.grid(
            row=row_number+3,
            column=0,
            columnspan=2,
            sticky="nsew"
            )
        window.bind("<Escape>", lambda event: list_chooser())

    change_theme(None, True)

    main_menu()

    window.mainloop()


if __name__ == "__main__":
    main()
