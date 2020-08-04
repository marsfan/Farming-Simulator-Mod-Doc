"""Clean up refs.

This absolutly awful looking piece of code will work its way through an xsd file and move single refs to be in-line
it is needed because trang really likes using xml refs, even when something is a single occurance.
It probably should be tidied up at some point.

To use, call from the command line, with at least one argument, and at most 2.
The first argument is the file to read in, the second is the file to write out to.
If the second argument is not specified from the command line, the program will write back to the file it read from.

NOTE: Sometimes it will not work quite right, and remove things before all substitutions. If this happens, I
recommend restoring the file, making a copy of it, and placing the missing refs back in.
This normally happens  if a ref is used in two different sections (i.e. another defined ref, and the main element).

It can also be called from another python file, by calling the processXSD function.
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
    count = 0

    # Set variable to a dummy value for now, so that the while loop runs properly on the first try.
    children = [1, 2]

    # Keep going through the file untill all segments have been checked. This will allow us to remove refs that
    # are used inside other refs that we decided to keep
    while len(children) > 1:

        schema: etree._ElementTree = etree.parse(infile)
        namespaces = {"xs": "http://www.w3.org/2001/XMLSchema"}
        children = list(schema.getroot())
        root = children.pop(0)
        for i in range(count):
            root = children.pop(0)
        refs = children
        for ref in refs:
            name = ref.attrib['name']
            elementsToReplace = root.findall(f'.//xs:element[@ref="{name}"]', namespaces)

            # Only replace references if they are only used once. If the reference is used more than once, it is actually
            # saving space for us, and can be left in place.
            if len(elementsToReplace) == 1:
                p = schema.getpath(elementsToReplace[0])
                p = replaceRegex.sub('', p)
                path = p.replace('/xs:schema/xs:element/', '')
                #path = p.replace('/xs:schema/xs:element[1]/', '').replace('/xs:schema/xs:element/', '')
                del elementsToReplace[0].attrib['ref']
                attribsToAdd = elementsToReplace[0].attrib
                elementToReplace = root.find(path, namespaces)

                #if elementToReplace is not None:
                elementToReplace.getparent().replace(elementToReplace, ref)

                root.find(path, namespaces).attrib.update(attribsToAdd)


        output = etree.tostring(schema, pretty_print=True)
        with open(outfile, 'wb') as f:
            f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write(output)
        count = count  + 1

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
