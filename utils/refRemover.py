"""Clean up refs.

This absolutly awful looking piece of code will work its way through an xsd file and move all refs to be in-line.
it is needed because trang really likes using xml refs, even when something is a single occurance.
It probably should be tidied up at some point.
"""


from lxml import etree
import argparse


def processXSD(infile: str, outfile: str) -> None:
    """Remove the use of refs in a XSD file."""

    schema: etree._ElementTree = etree.parse(infile)
    namespaces = {"xs": "http://www.w3.org/2001/XMLSchema"}
    children = list(schema.getroot())
    root = children.pop(0)
    refs = children
    for ref in refs:
        name = ref.attrib['name']
        elementsToReplace = root.findall(f'.//xs:element[@ref="{name}"]', namespaces)

        # Only replace references if they are only used once. If the reference is used more than once, it is actually
        # saving space for us, and can be left in place.
        if len(elementsToReplace) == 1:
            p = schema.getpath(elementsToReplace[0])
            path = p.replace('/xs:schema/xs:element[1]/', '').replace('/xs:schema/xs:element/', '')
            del elementsToReplace[0].attrib['ref']
            attribsToAdd = elementsToReplace[0].attrib
            elementToReplace = root.find(path, namespaces)
            elementToReplace.getparent().replace(elementToReplace, ref)

            root.find(path, namespaces).attrib.update(attribsToAdd)


    output = etree.tostring(schema, pretty_print=True)
    with open(outfile, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(output)


def main():
    """Function to run when called directly from CLI."""

    parser = argparse.ArgumentParser(description='Get rid of local refs in schema file')
    parser.add_argument("infile", type=str, help="Path to the file to process")
    parser.add_argument("outfile", type=str, help="Path to output result")
    args = parser.parse_args()

    processXSD(args.infile, args.outfile)


if __name__ == "__main__":
    main()
