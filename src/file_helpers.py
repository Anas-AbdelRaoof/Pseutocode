from sys import argv, exit
import os
try:
    from rich import print
except ModuleNotFoundError:
    print("Please download requirements.txt by <pip install -r requirements.txt --break-system-packages>")
    exit()
import json


def read_file():
    """Reads the file and uses other functions to handel errors"""

    try:
        pseudocode_file = argv[1]  # The text file that contains pseudocode
        with open(pseudocode_file, "r") as file:
            check_file_txt(file.name)
            return read_file_content(file)  # The pseudocode

    except FileNotFoundError:
        print(f"[red]File [italic blue]<{pseudocode_file}>[/italic blue] not found[/red]")
        exit()


def argv_length():
    """Checks the length of input arguments"""

    if len(argv) != 4:
        print("[red]Not enough input arguments[/red]")
        exit()


def check_file_txt(file):
    """Checks if the file is a .txt file and is not empty"""

    if not file.endswith(".txt"):
        print(f"[red]File [italic blue]<{file}>[/italic blue] must be a .txt file[/red]")
        exit()
    else:
        is_empty_file(file)


def is_empty_file(file):
    """is_empty_file checks for if the file with no content, if there is no content it output error message"""

    if os.path.getsize(file) == 0:
        print(f"[red]File [italic blue]<{file}>[/italic blue] is empty[/red]")
        exit()


def read_file_content(file):
    """Reading simply the file.txt"""

    return file.read()


def programming_language_name():
    """Returns the name of Programming language by lower()ing it"""

    return argv[2].lower()


def programming_language_file():
    """
    Returns Programming language file
    Notice: the file will be lower()
    """

    return argv[3].lower()


def programming_language_tips():
    """Returns the tips of chosen programming language"""

    name = programming_language_name()
    with open("languages.json", "r") as file:
        languages = json.load(file)
    lang = languages[name]
    tip = lang["tips"]
    return tip
