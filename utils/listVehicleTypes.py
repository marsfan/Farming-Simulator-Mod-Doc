"""List all of the different types of vehicles in vehicle files.

Used to add a restriction to the type attribute in vehicle.xsd.

"""

from pathlib import Path
import argparse
from typing import Set
import re

typeRegex = re.compile(r"type=\"([A-z]*)\">")



def main():
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    args = parser.parse_args()

    dataPath = Path(args.dataFolder)
    xmlFiles = dataPath.glob('vehicle/*.xml')

    vehicleTypes: Set[str] = set()

    for xmlFile in xmlFiles:
        with open(xmlFile) as fileObj:
            next(fileObj)
            fileData = next(fileObj)
            # Some files have a blank line before data starts. This skips over that if it is there.
            if fileData == '\n':
                fileData = next(fileObj)
            vehicleType: re.Match = typeRegex.search(fileData)
            if vehicleType is None:
                vehicleTypes.add("None")
            else:
                vehicleTypes.add(vehicleType.group(1))

    [print(vehicleType) for vehicleType in vehicleTypes]



if __name__=="__main__":
    main()
