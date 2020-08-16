"""List all of the different types of vehicles in vehicle files.

Used to add a restriction to the type attribute in vehicle.xsd.

"""

from pathlib import Path
import argparse
from typing import Optional, Set
import re

typeRegex = re.compile(r"<vehicle.*type=\"([^\"]*)\".*>")


def checkVehicleType(fileData: Path) -> Optional[str]:
    """Check the vehicle type for a single file

    Args:
        fileData: Contents of the file to check

    Returns:
        The vehicle type as a string

    """



    vehicleType: re.Match = typeRegex.search(fileData)

    if vehicleType is None:
        return None
    return vehicleType.group(1)


def main():
    """Run if directly called from command line."""
    parser = argparse.ArgumentParser(description="Sort FS2019 xml files by type")
    parser.add_argument("dataFolder", type=str, help="Data directory to sort")
    args = parser.parse_args()

    dataPath = Path(args.dataFolder)
    xmlFiles = dataPath.glob('**/*.xml')

    vehicleTypes: Set[str] = set()

    for xmlFile in xmlFiles:
        vehicleType = checkVehicleType(xmlFile)
        vehicleTypes.add(vehicleType.group(1))

    [print(vehicleType) for vehicleType in vehicleTypes]



if __name__=="__main__":
    main()
