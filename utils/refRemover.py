"""Clean up refs.

This absolutly awful looking piece of code will work its way through an xsd file and move single refs to be in-line
it is needed because trang really likes using xml refs, even when something is a single occurance.
It probably should be tidied up at some point.

To use, call from the command line, with at least one argument, and at most 2.
The first argument is the file to read in, the second is the file to write out to.
If the second argument is not specified from the command line, the program will write back to the file it read from.


It can also be called from another python file, by calling the processXSD function.

WARNING: If a element references a parent element in recursion--such as when trang is confused by multiple levels
of elements having the same name--this script can enter an infinite loop. With the base game files, this happens with
objects.xsd, so edit that one manually instead of with this script
"""


from lxml import etree
import argparse
import re
import os
from pathlib import Path

from lxml.etree import XMLParser

replaceRegex = re.compile(r'/xs:schema/xs:element\[.\]/')


def processXSD(infile: str, outfile: str) -> None:
    """Remove single-use refs in xsd file.

    Args:
        infile: File to read in from
        outfile: File to write out to

    """

    def getEl(elementPath: str) -> etree._Element:
        """Get an element in the XML tree from its path.

        This is needed to make sure we are editing the item in the schema, instead of a copy
        """
        # Make sure to remove "xs:schema" as for some reason find does not work if we have it.
        # Also make sure to include the xs namespace.
        return schema.xpath(elementPath, namespaces={"xs": "http://www.w3.org/2001/XMLSchema"})[0]


    # Load in the XSD file and then get the root elements.
    # Make sure the parser know to remove comments so they do not cause glitches
    schema: etree._ElementTree = etree.parse(infile)
    rootElements = list(schema.getroot())
    # Iterate backwards through all root element. (Backwards works better for some reason. )
    for rootElement in reversed(rootElements):
        try:
            name = rootElement.attrib['name']  # Get the name of the root element
        except KeyError:
            continue
        # Find all elements that reference this root element
        elementsToReplace = schema.xpath(
            f'.//xs:element[@ref="{name}"]', namespaces={"xs": "http://www.w3.org/2001/XMLSchema"})

        # Only replace references if they are only used once. If the reference is used more than once, it is actually
        # saving space for us, and can be left in place.
        if len(elementsToReplace) == 1:
            # Move single element out of list for ease of use.

            # Since writing to the elementsToReplace variable will not replace it in the actual schema, we need to
            # get the actual path to it, and use that to resolve the actual element.
            # We also need to stripe the "xs:schema" part of the path for some reason I don't really get.
            path = schema.getpath(elementsToReplace[0])
            elementToReplace = getEl(path)

            # Store the attribs that the the element has, so we can put them back in after replacing it
            oldAttribs = elementToReplace.attrib
            # Replace the element with the root element it references
            getEl(path).getparent().replace(elementToReplace, rootElement)
            # Add proper name attribute to the element.
            getEl(path).attrib['name'] = name

            # Add old attribs back in
            getEl(path).attrib.update(oldAttribs)

            # Remove ref attribute.
            del getEl(path).attrib['ref']

    # Convert the XSD into a string for exporting.
    output = etree.tostring(schema, pretty_print=True)

    # Write the XSD to the output file.
    with open(outfile, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(output)


def main():
    """Function to run when called directly from CLI."""

    # Use the argparse library to process arguments from the command line.
    parser = argparse.ArgumentParser(description='Get rid of local refs in schema file')
    parser.add_argument("infile", type=str, help="Path to the file to process")
    parser.add_argument("outfile", type=str,
                        help="Path to output result. If not given, will overwrite input file", nargs="?")
    args = parser.parse_args()

    # If user does not supply an output file, output to the file that was originally read from.
    if args.outfile is None:
        args.outfile = args.infile

    # If the path the user supplies for the input is a directory, run on all XSD files in that directory.
    if os.path.isdir(args.infile):
        if not os.path.isdir(args.outfile):
            TypeError("If input is a folder, output should be too")
        else:
            for file in Path(args.infile).glob(r"*.xsd"):
                print(f"Processing {file.name}")
                processXSD(str(file), str(Path(args.outfile) / file.name))
    else:
        # Call the XSD processing function.
        processXSD(args.infile, args.outfile)







if __name__ == "__main__":
    main()
