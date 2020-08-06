"""Count the number of occurances of the todo directive in documentation rst files.

Searches through the documentation folder of this repository for files with the extension .rst and then counts how many
times the directive `.. todo::` occurs in them. Returns to the command line the number of occurances of the directive.
This file is used for a github action that creates a custom badge on the project's readme file to keep track of the
number of todo directives remaining.
"""

from pathlib import Path
import sys
import re

todoRegex = re.compile(r"\.\. todo::")


def countTODOs() -> None:
    """Bundle task as function so that it can be called from other stuff."""
    totalTODOs = 0
    docPath = Path("./docs")
    rstFiles = docPath.glob("**/*.rst")

    for file in rstFiles:
        with open(file) as fileObj:
            totalTODOs += len(todoRegex.findall(fileObj.read()))

    sys.stdout.write(str(totalTODOs))

if __name__ == "__main__":
    countTODOs()
