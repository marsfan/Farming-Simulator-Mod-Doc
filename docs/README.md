# Documentation Folder

This folder contains the rst files that define the actual documentation pages.

There are a few special things to note that have been setup to simplify XML documentation, and future proofing the
files in the event that other versions of Farming Simulator are documented.


## File and Folder Structure.
The current folder serves as the top level directory for documentation. It contains the `index.rst` and a page for each
version of Farming Simulator.

There is then a seperate folder for each Farming Simulator Version. Inside that folder, there is a sigle file for each
category. Additionally, there are subfolders for each category. Right now, that means that there is only a FS2019
folder, and inside is is only `xml.rst` and a folder (`XML`) with documentation for the XML files.

This somewhat complicated folder structure was created for future-proofing. In the event that the documentation expands
to cover other aspects of modding, or other versions of Farming Simulator, the directory strucure will not need to be
refactored.

## Custom Directives
To adapt Sphinx to use the same terminology, a new directive was created: `.. element::`. This directive inherits from
the Python doman's `.. class::` directive. Becuase of this, it works in the exact same way as that directive, with
a single modification: Inclusion of a `:attrib ____:` field type. This functions identically to the `:param  ____`
field type in the `.. class::` directive, but just has a different name.

In the future, as the documentation expands, more directives may be added. Furthermore, a custom XML domain may be
created to simplify the process.

## XML Documentation Structure
Each XML documentation file is based off of a single XML Schema file. Normally this is straightforward, documenting how
elements are nested, and what each elements attribute's are. However, sometimes the same set of elements is used in
multiple places in the schema file. When this happens, that group of elements is placed seperatly in the schema file,
reducing the file size.  When this happens, documentation is done the same way. A seperate category is created called
(Elements Used Multiple Times in File) that documents these elements, and the primary element links to them.
For an example of this, see the documentating for wheel files ([./FS2019/XML/wheel.rst](FS2019/XML/wheel.rst)).