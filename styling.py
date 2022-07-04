import json
import os

FILE_PATH = os.path.dirname(os.path.realpath(__file__))

with open(f"{FILE_PATH}/Dependencies/user_settings.json", "r") as file:
    user_settings = json.load(file)
    file.close()


class ThemeChanger:

    __slots__ = ["style", "window"]

    def __init__(self, window, style):
        self.style = style
        self.window = window

    def change_theme(self, theme, bypass=False):
        global default_background
        global default_text_colour

        def darkmode(self, window, style):
            global default_background
            global default_text_colour
            window.configure(background="#1c1c1c")
            style.theme_use("default")
            style.map(
                'TButton', background=[('active', '#212121')],
                foreground=[('disabled', 'black')]
                )
            style.map("Green.TButton", background=[('active', '#009109')])
            style.map("Red.TButton", background=[("active", "#CC0000")])
            style.map(
                'Success.TButton', background=[('active', '#00ff00')],
                foreground=[('disabled', 'white')]
                )
            style.map('TCheckbutton', background=[('active', '#232323')])
            style.map(
                'Error.TButton', background=[('active', '#ff0000')],
                foreground=[('disabled', 'white')]
                )
            # The fix for the Treeview was found on this stack overflow article
            # https://stackoverflow.com/questions/58063067/unable-to-change-background-color-of-treeview-in-python
            style.map(
                "Treeview",
                foreground=[('disabled', '#a3a3a3'), ('selected', '#ffffff')],
                background=[('disabled', '#d9d9d9'), ('selected', '#4a6984')]
                )
            style.map("TCombobox", foreground=[('disabled', '#a3a3a3')])
            style.configure(
                "TButton", foreground="white", background="#1E1E1E",
                font="Helvetica 20", padding="5 5 5 5", wraplength=5000,
                anchor="center", relief="groove", borderwidth=2,
                bordercolor="black"
                )
            style.configure("Green.TButton", background="#008C0B")
            style.configure("Red.TButton", background="#C60000")
            style.configure(
                "Question.TButton", foreground="white"
                )
            style.configure(
                "Header.TButton", foreground="white"
                )
            style.configure(
                "Success.TButton", foreground="black", background="#009B0F",
            )
            style.configure(
                "Error.TButton", foreground="white", background="#FF0000",
            )
            style.configure(
                "TLabel", foreground="white", background="#1c1c1c",
                font="Helvetica 12", anchor="center", wraplength=5000
                )
            style.configure(
                "SubHeading.TLabel", foreground="white", background="#1c1c1c",
                font="Helvetica 16", anchor="center"
                )
            style.configure(
                "Header.TLabel", foreground="white", background="#1c1c1c",
                font="Helvetica 20", anchor="center"
                )
            style.configure(
                "Bold.TLabel", foreground="white", background="#1c1c1c",
                font=("Helvetica", 20, "bold"), anchor="center"
                )
            style.configure(
                "Title.TLabel", foreground="white", background="#1c1c1c",
                font="Helvetica 30", anchor="center"
                )
            style.configure(
                "Error.TLabel", foreground="white", background="red",
                font="Helvetica 24", anchor="center"
                )
            style.configure(
                "Success.TLabel", foreground="black", background="#00FF21",
                font="Helvetica 24", anchor="center"
                )
            style.configure(
                "Treeview", foreground="white", background="#232323",
                font="Helvetica 20", anchor="center", justify="center",
                rowheight=30, fieldbackground="#1c1c1c"
                )
            style.configure(
                "TFrame", foreground="white", background="#1c1c1c"
                )
            style.configure(
                "TScrollbar", foreground="white", background="#1c1c1c"
                )
            style.configure(
                "TProgressbar", foreground="white", background="#1c1c1c"
                )
            style.configure(
                "TCheckbutton", foreground="white", background="#1c1c1c",
                font="Helvetica 12"
                )
            style.configure(
                "TEntry", anchor="center", fieldbackground="#232323",
                foreground="white"
                )
            style.configure(
                "Header.TListbox", foreground="white", background="#1c1c1c",
                font="Helvetica 20", padding="5 5 5 5"
                )
            style.configure(
                "Vertical.Header.TScrollbar", foreground="white",
                background="#1c1c1c", font="Helvetica 12", padding="5 0 5 0"
                )
            style.configure(
                "TCombobox", foreground="black", background="#1c1c1c",
                font="Helvetica 16", padding="5 5 5 5"
                )
            default_background = "#1c1c1c"
            default_text_colour = "white"
            user_settings["Settings"][0]["colourScheme"] = "dark"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()

        def lightmode(self, window, style):
            global default_background
            global default_text_colour
            window.configure(background="#F0F0F0")
            style.theme_use("default")
            style.map('TButton', background=[('active', '#E0E0E0')])
            style.map('Green.TButton', background=[('active', '#8BF996')])
            style.map("Red.TButton", background=[("active", "#FF6060")])
            style.map(
                'Success.TButton', background=[('active', '#00ff00')],
                foreground=[('disabled', 'black')]
                )
            style.map(
                'Error.TButton', background=[('active', '#ff0000')],
                foreground=[('disabled', 'white')]
                )
            style.map('TCheckbutton', background=[('active', '#E0E0E0')])
            style.map(
                "Treeview",
                foreground=[('disabled', '#a3a3a3'), ('selected', '#ffffff')],
                background=[('disabled', '#d9d9d9'), ('selected', '#4a6984')]
                )
            style.configure(
                "TButton", foreground="black", background="#EAEAEA",
                font="Helvetica 20", padding="5 5 5 5", wraplength=5000,
                anchor="center", relief="groove", borderwidth=2,
                bordercolor="black"
                )
            style.configure("Green.TButton", background="#8EFF9B")
            style.configure("Red.TButton", background="#FF6868")
            style.configure(
                "Question.TButton", foreground="black"
                )
            style.configure(
                "Header.TButton", foreground="black"
                )
            style.configure(
                "Success.TButton", foreground="black", background="#00FF21",
            )
            style.configure(
                "Error.TButton", foreground="white", background="#FF0000",
            )
            style.configure(
                "TLabel", foreground="black", background="#F0F0F0",
                font="Helvetica 12", anchor="center", wraplength=5000
                )
            style.configure(
                "SubHeading.TLabel", foreground="black", background="#F0F0F0",
                font="Helvetica 16", anchor="center"
                )
            style.configure(
                "Header.TLabel", foreground="black", background="#F0F0F0",
                font="Helvetica 20", anchor="center"
                )
            style.configure(
                "Bold.TLabel", foreground="black", background="#F0F0F0",
                font=("Helvetica", 20, "bold"), anchor="center"
                )
            style.configure(
                "Title.TLabel", foreground="black", background="#F0F0F0",
                font="Helvetica 30", anchor="center"
                )
            style.configure(
                "Error.TLabel", foreground="white", background="red",
                font="Helvetica 24", anchor="center"
            )
            style.configure(
                "Success.TLabel", foreground="black", background="#00FF21",
                font="Helvetica 24", anchor="center"
            )
            style.configure(
                "Treeview", foreground="black", background="#F7F7F7",
                font="Helvetica 20", anchor="center", justify="center",
                rowheight=30, fieldbackground="#F0F0F0"
                )
            style.configure(
                "TFrame", foreground="black", background="#F0F0F0"
                )
            style.configure(
                "TScrollbar", foreground="black", background="#F0F0F0"
                )
            style.configure(
                "TProgressbar", foreground="black", background="#F0F0F0"
                )
            style.configure(
                "TCheckbutton", foreground="black", background="#F0F0F0",
                font="Helvetica 12"
                )
            style.configure(
                "TEntry", anchor="center", fieldbackground="#F7F7F7",
                foreground="black"
                )
            style.configure(
                "Header.TListbox", foreground="black", background="#F0F0F0",
                font="Helvetica 20", padding="5 5 5 5"
                )
            style.configure(
                "Vertical.Header.TScrollbar", foreground="black",
                background="#F0F0F0", font="Helvetica 12", padding="5 5 5 5"
                )
            style.configure(
                "TCombobox", foreground="black", background="#F0F0F0",
                font="Helvetica 16", padding="5 5 5 5"
                )
            default_background = "#F0F0F0"
            default_text_colour = "black"
            user_settings["Settings"][0]["colourScheme"] = "light"
            with open(
                f"{FILE_PATH}/Dependencies/user_settings.json", "w"
                    ) as file:
                json.dump(user_settings, file, indent=4)
                file.close()

        if theme == "#1c1c1c" and bypass is not True:
            lightmode(self, self.window, self.style)

        elif theme == "#F0F0F0" and bypass is not True:
            darkmode(self, self.window, self.style)

        elif user_settings["Settings"][0]["colourScheme"] == "dark":
            darkmode(self, self.window, self.style)

        elif user_settings["Settings"][0]["colourScheme"] == "light":
            lightmode(self, self.window, self.style)

    def default_colours(self, theme, area) -> str:
        if theme == "dark":
            if area == "background":
                return "#1c1c1c"
            elif area == "foreground":
                return "white"
            elif area == "entrybg":
                return "#232323"
            elif area == "entrybg2":
                return "#1E1E1E"
        elif theme == "light":
            if area == "background":
                return "#F0F0F0"
            elif area == "foreground":
                return "black"
            elif area == "entrybg":
                return "#F7F7F7"
            elif area == "entrybg2":
                return "#EFEFEF"
        return ""


if __name__ == "__main__":
    pass
