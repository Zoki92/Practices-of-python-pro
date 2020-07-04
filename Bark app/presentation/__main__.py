import os, sys


# DIR PATH: D:\Environments\practices of the python pro\Bark app\presentation
dir_path = os.path.dirname(os.path.realpath(__file__))

# PARENT DIR PATH: D:\Environments\practices of the python pro\Bark app
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0, parent_dir_path)
# the previous three commands were added because it doesn't recognize imports
# reason is because __main__ doesn't recognize that is part of a package
# so we add it's path to sys
from collections import OrderedDict

from business_logic import commands


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name
        self.command = command
        self.prep_call = prep_call

    def choose(self):
        data = self.prep_call() if self.prep_call else None
        message = self.command.execute(data) if data else self.command.execute()
        print(message)

    def __str__(self):
        return self.name


def print_options(options):
    for shortcut, option in options.items():
        print(f"({shortcut}) {option}")
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options


def get_option_choice(options):
    choice = input("Choose an option: ")
    while not option_choice_is_valid(choice, options):
        print("Invalid choice")
        choice = input("Choose an option: ")
    return options[choice.upper()]


def get_user_input(label, required=True):
    value = input(f"{label}: ") or None
    while required and not value:
        value = input(f"{label}: ") or None
    return value


def get_new_bookmark():
    return {
        "title": get_user_input("Title"),
        "url": get_user_input("URL"),
        "notes": get_user_input("Notes", required=False),
    }


def get_bookmark_id_for_deletion():
    return get_user_input("Enter bookmark ID to delete:  ")


def clear_screen():
    clear = "cls" if os.name == "nt" else "clear"
    os.system(clear)


def get_github_import_options():
    return {
        "github_username": get_user_input("Github username"),
        "preserve_timestamps": get_user_input(
            "Preserve timestamps [Y/n]", required=False
        )
        in {"Y", "y", None,},
    }


def get_new_bookmark_info():
    bookmark_id = get_user_input("Enter a bookmark ID to edit")
    field = get_user_input("Choose a value to edit (title, URL, notes)")
    new_value = get_user_input(f"Enter the new value for {field}")
    return {
        "id": bookmark_id,
        "update": {field: new_value},
    }


def loop():

    clear_screen()
    options = OrderedDict(
        {
            "A": Option(
                "Add a bookmark",
                commands.AddBookMarkCommand(),
                prep_call=get_new_bookmark,
            ),
            "B": Option("List bookmarks by date", commands.ListBookmarksCommand()),
            "C": Option(
                "List bookmarks by title",
                commands.ListBookmarksCommand(order_by="title"),
            ),
            "D": Option(
                "Delete a bookmark",
                commands.DeleteBookmarkCommand(),
                prep_call=get_bookmark_id_for_deletion,
            ),
            "E": Option(
                "Update single bookmark",
                commands.EditBookmarkCommand(),
                prep_call=get_new_bookmark_info,
            ),
            "G": Option(
                "Import github stars",
                commands.ImportGitHubStarsCommand(),
                prep_call=get_github_import_options,
            ),
            "Q": Option("Quit", commands.QuitCommand(),),
        }
    )

    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input("Press Enter to return to menu")


if __name__ == "__main__":
    commands.CreateBookmarksTableCommand().execute()
    while True:
        loop()
