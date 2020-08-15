"""List all of the placeable types in a folder."""

import argparse
from pathlib import Path
from typing import Set

import re

typeRegex = re.compile(r"<placeableType>(\w*)</placeableType>")


def main():
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    args = parser.parse_args()

    dataPath = Path(args.dataFolder)
    xmlFiles = dataPath.glob('*.xml')

    placeableTypes: Set[str] = set()

    for xmlFile in xmlFiles:
        with open(xmlFile) as fileObj:
            fileData = fileObj.read()
            # Some files have a blank line before data starts. This skips over that if it is there.
            placeableTypes.add(typeRegex.search(fileData).group(1))

    [print(placeableType) for placeableType in placeableTypes]


if __name__ == "__main__":
    main()
