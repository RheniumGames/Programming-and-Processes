# A revision tool that can use user created questions and answers and present
# them in a quiz format.

import json
import os
import random
import time
import tkinter as tk
import typing
from tkinter import ttk
from typing import List
from styling import ThemeChanger

# Global variables
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
questions = []
choices = []
answers = []
current_choices: List[str] = []
default_background = ''
default_text_colour = ''
score = 0

# Loads the user information from the corresponding json file
try:
    with open(f"{FILE_PATH}/Dependencies/user_settings.json", "r") as file:
        user_settings = json.load(file)
        file.close()
except FileNotFoundError as error:
    with open(f"{FILE_PATH}/Dependencies/user_settings.json", "w") as file:
        json.dump({
            "Settings": [
                {
                    "colourScheme": "light"
                }
            ],
            "QuizData": [
                {
                    "totalScore": 0
                }
            ]
        }
        , file, indent=4)
        file.close()
        print(error)
    with open(f"{FILE_PATH}/Dependencies/user_settings.json", "r") as file:
        user_settings = json.load(file)
        file.close()

# More global variables
globalscore = user_settings["QuizData"][0]["totalScore"]
theme = user_settings["Settings"][0]["colourScheme"]

# Custom error handling
class NoFileNameError(Exception):
    pass

class NoQuestionError(Exception):
    pass

class NoAnswerError(Exception):
    pass

class NoChoiceError(Exception):
    pass


# Define the main function
def main():
    row_number = 1
    window = tk.Tk()
    window.title("Revision Tool")
    WIDTH = 1280
    HEIGHT = 720
    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(False, False)
    style = ttk.Style()

    styling=ThemeChanger(window, style)

    def collect_default() -> None:
        global default_background
        global default_text_colour
        default_background = styling.default_colours(theme, "background")
        default_text_colour = styling.default_colours(theme, "foreground")
        return
    
    def error_message(window, text, seconds) -> None:
        message = ttk.Label(
            window,
            text=text,
            style="Error.TLabel"
        )
        message.place(
            x=WIDTH / 4,
            y=HEIGHT / 4,
            width=WIDTH / 2,
            height=HEIGHT / 2
        )
        message.after(int(seconds * 1000), lambda: message.destroy())
        return
    
    def success_message(window, text, seconds) -> None:
        message = ttk.Label(
            window,
            text=text,
            style="Success.TLabel"
        )
        message.place(
            x=WIDTH / 4,
            y=HEIGHT / 4,
            width=WIDTH / 2,
            height=HEIGHT / 2
        )
        message.after(int(seconds * 1000), lambda: message.destroy())
        return

    def error_button(button, text, seconds) -> None:
        button.config(
            text=text,
            style="Error.TButton",
            state="disabled"
        )
        button.after(
            int(seconds * 1000),
            lambda: button.config(
                text="Submit", state="normal", style="Header.TButton"
                )
            )
        return
    
    def success_button(button, text, seconds) -> None:
        button.config(
            text=text,
            style="Success.TButton",
            state="disabled"
        )
        button.after(
            int(seconds * 1000),
            lambda: button.config(
                text="Submit", state="normal", style="Header.TButton"
                )
            )
        return
    
    def dump_questions(question, answer, choices, filename, element):
        try:
            if (filename == "" or filename is None or
                filename.lower() == "enter a file name"):
                raise NoFileNameError
            if question == "":
                raise NoQuestionError
            if "" in choices:
                raise NoChoiceError
            # Dumps the questions into the questions.json file
            correct_list = []
            correct_list_words = []
            # Extract 'selected' from tuple, and set empty tuples to 0
            for i in answer:
                try:
                    if "selected" in i:
                        correct_list.append("1")
                    else:
                        correct_list.append("0")
                except IndexError:
                    correct_list.append("0")
            print(correct_list)
            if '1' not in correct_list:
                raise NoAnswerError

            # Loop through correct list, if there is a 1 in the list,
            # add the corresponding text in answers to correct_list_words
            filename = filename.replace(".json", "").lower()
            for i in range(len(correct_list)):
                if correct_list[i] == "1":
                    correct_list_words.append(choices[i])
            try:
                with open(
                    f"{FILE_PATH}/Dependencies/{filename}.json", "r"
                        ) as file:
                    try:
                        data = json.load(file)
                    except json.decoder.JSONDecodeError:
                        data: dict[str, ...] = {}
                    file.close()
            except FileNotFoundError:
                with open(
                    f"{FILE_PATH}/Dependencies/{filename}.json", "w"
                        ) as file:
                    data: dict[str, ...] = {}
                    file.close()

            if "QuestionList" not in data:
                data["QuestionList"] = []
            data["QuestionList"].append(
                {
                    "question": question,
                    "options": choices,
                    "answer": str(correct_list_words[0])
                    }
                )
            with open(
                f"{FILE_PATH}/Dependencies/{filename}.json", "w"
                    ) as file:
                json.dump(data, file, indent=4)
                file.close()
            success_button(element, "Question added successfully!", 1.5)
        except NoFileNameError:
            error_button(element, "Please enter a file name", 1.5)
        except NoQuestionError:
            error_button(element, "Please enter a question", 1.5)
        except NoAnswerError:
            error_button(element, "Please select an answer", 1.5)
        except NoChoiceError:
            error_button(element, "Please create four choices", 1.5)
        return

    def main_menu():
        window.columnconfigure([0, 1], weight=0)
        window.columnconfigure([0], weight=1, uniform="group2")
        window.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], weight=0)
        window.rowconfigure([0, 1, 2], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()

        title = ttk.Label(
            window, text="Quiz Program", style="Title.TLabel"
        )
        title.grid(row=0, column=0, columnspan=2)
        start_button = ttk.Button(
            window, text="Start", command=lambda: list_chooser(),
            style="Header.TButton"
        )
        start_button.grid(row=1, column=0, sticky="n")
        question_maker_button = ttk.Button(
            window, text="Question Maker", command=lambda: question_maker(),
            style="Header.TButton"
        )
        question_maker_button.grid(row=1, column=0)
        theme_change_button = ttk.Button(
            window, text="Change Theme",
            command=lambda: styling.change_theme(window.cget("bg"), False),
            style="Header.TButton"
        )
        theme_change_button.grid(row=2, column=0)
        theme_change_button.bind("<Button-1>", lambda event: collect_default())
        scorelabel = ttk.Label(
            window,
            text="Over all of your attempts, you have scored: "
            f"{globalscore} points",
            style="SubHeading.TLabel",
            padding="15"
        )
        scorelabel.grid(row=3, column=0)
        window.bind("<Escape>", lambda event: window.destroy())

    def question_maker():
        # This function will bring up a GUI that will allow users to make
        # Their own questions.
        window.columnconfigure([0, 1], weight=1)
        window.rowconfigure([0, 1, 3], weight=0)
        window.rowconfigure([2, 4, 7], weight=1)
        for i in window.grid_slaves():
            i.grid_forget()
        file_name = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        file_name.insert(0, "Enter a file name")
        print(file_name.get())
        def delete_filename(text):
            if text == "Enter a file name":
                file_name.delete(0, "end")
            else:
                pass
        file_name.bind(
            "<Button-1>",
            lambda event: delete_filename(file_name.get())
            )
        file_name.grid(row=0, column=0, columnspan=2)
        user_question_header = ttk.Label(
            window, text="Enter your question here:", style="Header.TLabel"
            )
        user_question_header.grid(
            row=1, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
            )
        back = ttk.Button(
            window, text="Back", command=lambda: main_menu(),
            style="Header.TButton", takefocus=0
            )
        back.grid(
            row=0,
            column=0,
            sticky="w",
            )
        user_question = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        user_question.grid(
            row=2, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
            )
        header_1 = ttk.Label(
            window, text="Enter the first choice:", style="SubHeading.TLabel"
        )
        header_1.grid(row=3, column=0, sticky="ew", padx=2, pady=2)
        answer_1 = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        answer_1.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
        correctmarker_1 = ttk.Checkbutton(
            window, text="Set Answer", style="TCheckbutton", takefocus=0
        )
        correctmarker_1.grid(
            row=5, column=0, sticky="sew", padx=2, pady=2
            )
        header_1 = ttk.Label(
            window, text="Enter the second choice:", style="SubHeading.TLabel"
        )
        header_1.grid(row=3, column=1, sticky="ew", padx=2, pady=2)
        answer_2 = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        answer_2.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
        correctmarker_2 = ttk.Checkbutton(
            window, text="Set Answer", style="TCheckbutton", takefocus=0
        )
        correctmarker_2.grid(
            row=5, column=1, sticky="sew", padx=2, pady=2
            )
        header_3 = ttk.Label(
            window, text="Enter the third choice", style="SubHeading.TLabel"
        )
        header_3.grid(row=6, column=0, sticky="ew", padx=2, pady=2)
        answer_3 = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        answer_3.grid(row=7, column=0, sticky="nsew", padx=5, pady=5)
        correctmarker_3 = ttk.Checkbutton(
            window, text="Set Answer", style="TCheckbutton", takefocus=0
        )
        correctmarker_3.grid(
            row=8, column=0, sticky="sew", padx=2, pady=2
            )
        header_4 = ttk.Label(
            window, text="Enter the fourth choice", style="SubHeading.TLabel"
        )
        header_4.grid(row=6, column=1, sticky="ew", padx=2, pady=2)
        answer_4 = ttk.Entry(
            window, style="TEntry", justify="center",
            font="Helvetica 16"
            )
        answer_4.grid(row=7, column=1, sticky="nsew", padx=5, pady=5)
        correctmarker_4 = ttk.Checkbutton(
            window, text="Set Answer", style="TCheckbutton", takefocus=0
        )
        correctmarker_4.grid(
            row=8, column=1, sticky="sew", padx=2, pady=2
            )
        correctmarker_1.state(["!alternate"])
        correctmarker_2.state(["!alternate"])
        correctmarker_3.state(["!alternate"])
        correctmarker_4.state(["!alternate"])
        # Collect whether check buttons are checked or not
        user_question_submit = ttk.Button(
            window, text="Submit", style="Header.TButton", takefocus=0,
            command=lambda: dump_questions(
                user_question.get(),
                [
                    correctmarker_1.state(),
                    correctmarker_2.state(),
                    correctmarker_3.state(),
                    correctmarker_4.state()
                ],
                [
                    answer_1.get(),
                    answer_2.get(),
                    answer_3.get(),
                    answer_4.get()
                ],
                file_name.get(),
                user_question_submit
            )
        )
        user_question_submit.grid(
            row=9, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
            )
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
        file_name = file_name.lower()
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
        header = ttk.Label(
            window, text="Select a file to import questions from:",
            style="Header.TLabel"
            )
        header.grid(
            row=0, column=0, columnspan=2, sticky="nsew", padx=5, pady=5
            )
        back = ttk.Button(
            window, text="Back", command=lambda: main_menu(),
            style="Header.TButton"
            )
        back.grid(
            row=0,
            column=0,
            sticky="w"
            )
        scrollbar = ttk.Scrollbar(
            window, orient="vertical"
            )
        scrollbar.grid(
            row=1,
            column=1,
            sticky="ns"
            )
        treeview = ttk.Treeview(
            window,
            columns=0,
            show="tree",
            displaycolumns=("0"),
            selectmode="extended",
            style="Treeview",
            yscrollcommand=scrollbar.set,
            )
        treeview.grid(
            row=1,
            column=0,
            sticky="nsew"
            )
        # https://stackoverflow.com/questions/8688839/remove-empty-first-column-of-a-treeview-object
        treeview.column("#0", width = 0, stretch="no")
        treeview.column(column=0, anchor="center")
        for i in file_list:
            print(i)
            treeview.insert("", "end", text=str(i), values=(i))
        treeview.bind("<Double-1>", lambda event: file_loader(
            treeview.item(treeview.selection())["values"][0]
            ))
        scrollbar.config(command=treeview.yview)
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
                for i in window.grid_slaves():
                    if i.grid_info()["row"] != 0 and i.grid_info()["row"] != 1:
                        i.grid_forget()
                window.rowconfigure([2, 3], weight=0)

        def check_answer(answer) -> int:
            global score
            global globalscore
            try:
                if answer == answers[0]:
                    score += 1
                    globalscore += 1
                    score_display.configure(text=f"Score: {str(score)}")
                    success_message(window, "Correct!", 0.5)
                else:
                    error_message(window, "Incorrect!", 0.5)
                answers[:1] = []
                new_question()
                return score
            except IndexError:
                return 0

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
            window, text="Back", command=lambda: list_chooser(),
            style="Header.TButton"
            )
        back.grid(
            row=0,
            column=0,
            sticky="w"
            )
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

    styling.change_theme(None, True)

    collect_default()

    main_menu()

    def quit_program():
        with open(
            f"{FILE_PATH}/Dependencies/user_settings.json", "r"
                ) as file:
            data = json.load(file)

        # Replace the old score with the new score
        data["QuizData"][0]["totalScore"] = globalscore
        with open(
            f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                ) as file:
            json.dump(data, file, indent=4)
            file.close()

        window.destroy()

    window.protocol("WM_DELETE_WINDOW", quit_program)

    window.mainloop()


if __name__ == "__main__":
    main()
