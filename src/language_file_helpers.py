import sys
try:
    from rich import print
except ModuleNotFoundError:
    print("Please download requirements.txt by <pip install -r requirements.txt --break-system-packages>")
    sys.exit()
import os
import json


def check_lang(language_name, language_file):
    """
    Validate that the given filename matches the expected file extension for the
    provided programming language name.

    Parameters
    - language_name: str
        Name of the programming language (e.g. "python", "javascript"). This
        function normalizes to lower-case before lookup, so callers may use any
        case.

    - language_file: str
        The filename to check (e.g. "example.py"). The function inspects the
        file extension and compares it with the expected extension for the
        language.

    Returns
    - True if the language is supported and the file has the expected
      extension.
    - False otherwise (and prints a helpful message explaining the mismatch).

    Behavior notes / implementation details
    - We use os.path.splitext to extract the file extension because it is
      robust to filenames with multiple dots (e.g. "archive.tar.gz").
    - The language lookup is case-insensitive (we call .lower() on the input
      language name prior to checking the dictionary).
    - The languages_extensions dictionary stores extensions with a leading dot
      so we can compare directly to the result of os.path.splitext.
    """

    try:
        with open("languages.json", "r") as file:
            languages = json.load(file)

        lang = languages[language_name]
        
        extension = lang["extension"]  # Language name's extension

        if not language_file.endswith(extension):  # Ex: name: Rust file: .lua
            print(
                f"""[red]File <[italic blue]{language_file}[/italic blue]> is not [italic blue]{language_name.title()}[/italic blue] file[/red]\n[green]Do you mean <[yellow]{language_file.replace(file_and_extension[1], languages_extensions[language_name].replace(".", ""))}[/yellow]>?[/green]""")
            return False

    except KeyError:
        print(
            f"[red]Language [italic blue]{language_name.title()}[/italic blue] is not allowed or not real language[/red]")
        return False

    return True
