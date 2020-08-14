"""For each root element in a XML file, count how many lines in the element.
The print out a list of the elements and the number of lines they have.
Optionally pass a flag to sort the elements by length
"""


from lxml import etree
import argparse
import re
import os
from pathlib import Path

from lxml.etree import XMLParser
from typing import Dict

replaceRegex = re.compile(r'/xs:schema/xs:element\[.\]/')


def countElements(infile: str, sort: bool = False) -> Dict[str, int]:
    """Count number of lines for each root element.

    Args:
        infile: File to read in from
        sort: Whether or not to sort the element by size

    Returns:
        A dict of all of the root elements and the number of lines they have.

    """


    elementCounts: Dict[str, int] = {}
    # Load in the XSD file and then get the root elements.
    # Make sure the parser know to remove comments so they do not cause glitches
    schema: etree._ElementTree = etree.parse(infile)
    rootElements = list(schema.getroot())
    # Iterate backwards through all root element. (Backwards works better for some reason. )
    for rootElement in rootElements:
        asText = etree.tostring(rootElement, pretty_print=True)
        newLineCount = len(re.findall(br"\n", asText))
        try:
            elementCounts[rootElement.attrib['name']] = newLineCount
        except KeyError:
            pass

    if sort:
        elementCounts = {k: v for k, v in sorted(elementCounts.items(), key=lambda item: item[1])}
    return elementCounts

def main():
    """Function to run when called directly from CLI."""

    # Use the argparse library to process arguments from the command line.
    parser = argparse.ArgumentParser(description='Count lines in each root element')
    parser.add_argument("infile", type=str, help="Path to the file to read")
    parser.add_argument("-s", "--sorted", action='store_true', help="Sort by line number")
    args = parser.parse_args()

    elementCounts = countElements(args.infile, args.sorted)
    for key, value in elementCounts.items():
        print(f"{value}:", key)

    print(f'{sum(elementCounts.values())}: Total')


if __name__ == "__main__":
    main()
