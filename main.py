# A revision tool that can use user created questions and answers and present
# them in a quiz format.

import tkinter


class InvalidList(Exception):
    pass


def import_list():
    try:
        raise InvalidList("This is filler text")
    except InvalidList as error:
        print(error)


def main():
    window = tkinter.Tk()
    window.title("Revision Tool")
    window.geometry("1280x720")
    import_list()
    window.mainloop()


if __name__ == "__main__":
    main()