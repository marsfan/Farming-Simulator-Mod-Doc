"""Collects all  xml files from game data and sorts them into folders based off of the vehicle type.

This makes generating schema files a little bit eaiser, as we then can generate schema files for each xml type
separately.
"""

import argparse
import os
from pathlib import Path
from typing import Union
import re
from shutil import copyfile

xmlRegex = re.compile(r"<([A-z]*)")
typeRegex = re.compile(r"type=\"([A-z]*)\">")


def main() -> None:
    """Run main code."""
    fileCount = 0
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    args = parser.parse_args()
    dataPath = Path(args.dataFolder)
    safeMakeDir("SortedXML")
    #safeMakeDir(Path("SortedXML") / "vehicle")
    xmlFiles = dataPath.glob('**/*.xml')
    print(len(list(xmlFiles)))

    for xmlFile in xmlFiles:
        break
        fileCount += 1
        with open(xmlFile) as fileObj:
            next(fileObj)
            fileData = next(fileObj)
            # Some files have a blank line before data starts. This skips over that if it is there.
            if fileData == '\n':
                fileData = next(fileObj)
            xmlType = xmlRegex.search(fileData).group(1)

            if xmlType == 'vehicle':
                vehicleType = typeRegex.search(fileData)
                if vehicleType is None:
                    copyDest = Path("SortedXML") / xmlType
                else:
                    vehicleType = vehicleType.group(1)
                    copyDest = Path("SortedXML") / xmlType / vehicleType
            else:
                copyDest = Path("SortedXML") / xmlType
       # print('------')
       # print(copyDest)
       # print(copyDest / xmlFile.name)
       # print('--------')
        safeMakeDir(copyDest)
        copyfile(xmlFile, copyDest / xmlFile.name)

    print(fileCount)


def safeMakeDir(dirToMake: Union[Path, str]) -> None:
    """Try to create a folder. Raise error if file exists at same path, but not if folder exists at same path."""
    if not os.path.exists(dirToMake):
        if os.path.isdir(dirToMake):
            raise FileExistsError(f"Folder ({dirToMake}) already exists as a file!")
        else:
            os.makedirs(dirToMake)


if __name__ == "__main__":
    main()
