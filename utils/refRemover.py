"""Clean up refs.

This absolutly awful looking piece of code will work its way through an xsd file and move single refs to be in-line
it is needed because trang really likes using xml refs, even when something is a single occurance.
It probably should be tidied up at some point.

To use, call from the command line, with at least one argument, and at most 2.
The first argument is the file to read in, the second is the file to write out to.
If the second argument is not specified from the command line, the program will write back to the file it read from.


It can also be called from another python file, by calling the processXSD function.

WARNING: If a element references a parent element in recursion--such as when trang is confused by multiple levels
of elements having the same name--this script can enter an infinite loop.
"""


from lxml import etree
import argparse
import re

replaceRegex = re.compile(r'/xs:schema/xs:element\[.\]/')


def processXSD(infile: str, outfile: str) -> None:
    """Remove single-use refs in xsd file.

    Args:
        infile: File to read in from
        outfile: File to write out to

    """
    schema: etree._ElementTree = etree.parse(infile)
    namespaces = {"xs": "http://www.w3.org/2001/XMLSchema"}
    children = list(schema.getroot())
    refs = children
    for ref in reversed(refs):
        name = ref.attrib['name']
        elementsToReplace = schema.findall(f'.//xs:element[@ref="{name}"]', namespaces)

        # Only replace references if they are only used once. If the reference is used more than once, it is actually
        # saving space for us, and can be left in place.
        if len(elementsToReplace) == 1:
            path = schema.getpath(elementsToReplace[0]).replace("xs:schema", '')

            elementsToReplace[0].attrib['name'] = elementsToReplace[0].attrib['ref']
            del elementsToReplace[0].attrib['ref']

            attribsToAdd = elementsToReplace[0].attrib
            elementToReplace = schema.find(path, namespaces)

            elementToReplace.getparent().replace(elementToReplace, ref)

            schema.find(path, namespaces).attrib.update(attribsToAdd)

    output = etree.tostring(schema, pretty_print=True)
    with open(outfile, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(output)

def main():
    """Function to run when called directly from CLI."""

    parser = argparse.ArgumentParser(description='Get rid of local refs in schema file')
    parser.add_argument("infile", type=str, help="Path to the file to process")
    parser.add_argument("outfile", type=str, help="Path to output result. If not given, will overwrite input file", nargs="?")
    args = parser.parse_args()
    if args.outfile is None:
        args.outfile = args.infile
    processXSD(args.infile, args.outfile)


if __name__ == "__main__":
    main()
