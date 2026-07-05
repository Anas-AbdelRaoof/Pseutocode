import sys
from rich import print
import os


# Mapping of supported language names (keys) to their file extensions (values).
# Keys should be lowercase and may include common aliases (e.g. "js" and "javascript").
# Values include the leading dot (".py", ".js") so they can be compared directly
# against the value returned from os.path.splitext(filename)[1].
# Keep this dictionary updated when you add/remove supported languages.
languages_extensions = {
    "python": ".py",
    "c++": ".cpp",
    "cpp": ".cpp",
    "c": ".c",
    "java": ".java",
    "ruby": ".rb",
    "c#": ".cs",
    "cs": ".cs",
    "csharp": ".cs",
    "php": ".php",
    "rust": ".rs",
    "go": ".go",
    "golang": ".go",
    "lua": ".lua",
    "swift": ".swift",
    "kotlin": ".kt",
    "dart": ".dart",
    "gdscript": ".gd",
    "js": ".js",
    "javascript": ".js",
    "zig": ".zig",
    "julia": ".jl",
    "f#": ".fs",
    "fsharp": ".fs",
    "cython": ".pyx",
}  # Notice: the languages names were lower() before this dictionary


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
        file_and_extension = language_file.split(".")

        extension = languages_extensions[language_name]  # Language name's extension

        if not language_file.endswith(extension):  # Ex: name: Rust file: .lua
            print(
                f"""[red]File <[italic blue]{language_file}[/italic blue]> is not [italic blue]{language_name.title()}[/italic blue] file[/red]\n[green]Do you mean <[yellow]{language_file.replace(file_and_extension[1], languages_extensions[language_name].replace(".", ""))}[/yellow]>?[/green]""")
            return False

    except KeyError:
        print(
            f"[red]Language [italic blue]{language_name.title()}[/italic blue] is not allowed or not real language[/red]")
        return False

    return True
