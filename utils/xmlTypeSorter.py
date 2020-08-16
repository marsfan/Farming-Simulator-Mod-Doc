"""Collects all  xml files from game data and sorts them into folders based off of the vehicle type.

This makes generating schema files a little bit eaiser, as we then can generate schema files for each xml type
separately.
"""

import argparse
import os
from pathlib import Path
from typing import Union
import re
from shutil import copy, copyfile
import listPlaceableTypes
import listVehicleTypes

xmlRegex = re.compile(r"<\?xml[^>]*>\n\n?<(\w*)[^>]*>")


def main() -> None:
    """Run main code."""
    fileCount = 0
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    parser.add_argument("-t", "--types", action="store_true", help="Sort Vehicle and Placeables by type")
    args = parser.parse_args()
    dataPath = Path(args.dataFolder)
    safeMakeDir("SortedXML")
    xmlFiles = dataPath.glob('**/*.xml')

    for xmlFile in xmlFiles:
        fileCount += 1
        with open(xmlFile) as fileObj:
            fileData = fileObj.read()
        xmlType = xmlRegex.search(fileData).group(1)
        copyDest: Path = Path("SortedXML") / xmlType
        if args.types:
            placeableType = listPlaceableTypes.checkPlaceableType(fileData)
            vehicleType = listVehicleTypes.checkVehicleType(fileData)
            if placeableType is not None:
                copyDest = copyDest / placeableType
            elif vehicleType is not None:
                copyDest = copyDest / vehicleType
        safeMakeDir(copyDest)
        copyfile(xmlFile, copyDest / xmlFile.name)

    print(f'Total Files Sorted: {fileCount}')


def safeMakeDir(dirToMake: Union[Path, str]) -> None:
    """Try to create a folder. Raise error if file exists at same path, but not if folder exists at same path."""
    if not os.path.exists(dirToMake):
        if os.path.isdir(dirToMake):
            raise FileExistsError(f"Folder ({dirToMake}) already exists as a file!")
        else:
            os.makedirs(dirToMake)


if __name__ == "__main__":
    main()
