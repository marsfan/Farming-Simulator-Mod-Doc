"""List all of the placeable types in a folder."""

import argparse
from pathlib import Path
from typing import Optional, Set

import re

typeRegex = re.compile(r"<placeableType>(\w*)</placeableType>")


def checkPlaceableType(fileData: str) -> Optional[str]:
    """Check the placeable type for a single file

    Args:
        fileData: Contents of the file to check

    Returns:
        The placeable type as a string

    """
    # Some files have a blank line before data starts. This skips over that if it is there.
    placeableType = typeRegex.search(fileData)
    if placeableType is None:
        return None
    return placeableType.group(1)

def main():
    """Run if directly called from command line."""
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    args = parser.parse_args()

    dataPath = Path(args.dataFolder)
    xmlFiles = dataPath.glob('**/*.xml')

    placeableTypes: Set[str] = set()

    for xmlFile in xmlFiles:
        with open(xmlFile) as fileObj:
            fileData = fileObj.read()
            # Some files have a blank line before data starts. This skips over that if it is there.
            placeableType = typeRegex.search(fileData)
            if placeableType is not None:
                placeableTypes.add(placeableType.group(1))



    [print(placeableType) for placeableType in placeableTypes]


if __name__ == "__main__":
    main()
