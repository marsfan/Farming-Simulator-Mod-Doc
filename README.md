
# FS2019-Mod-Doc

[![](https://byob.yarr.is/Marsfan/Farming-Simulator-Mod-Doc/todoCount)](https://farming-simulator-mod-doc.readthedocs.io/en/latest/todo.html)
[![Documentation Status](https://readthedocs.org/projects/farming-simulator-mod-doc/badge/?version=latest)](https://farming-simulator-mod-doc.readthedocs.io/en/latest/?badge=latest)

Documentation on everything to do with modding Farming Simulator.

This project aims to eventually have complete documentation of all of XML elements used for modding Farming Simulator 2019. \
Stretch goals include adding documentation for all prior version of Farming Simulator, and adding documentation regarding other parts of modding Farming Simulator (textures, animations, lua, etc)



## Repository Structure

### .github
The `.github` folder contains configuration files for hosting this project on GitHub.\
It contains the code of conduct file ([`CODE_OF_CONDUCT.md`](./.github/CODE_OF_CONDUCT.md)), as well as the pull request template ([`pull_request_template.md`](.github/pull_request_template.md))

Additionally, it contains teh following folders:

#### ISSUE_TEMPLATE
Contains templates for issues  in github

#### workflows
Contains yaml files for defineing GitHub Actions

### docs
Contains the `rst` files that define the entire documentation site, as well as the configuration files for Sphinx (the documentation generation framework).

For more information about the layout of the documentation folder, see [docs/readme.md](docs/README.md).

### schemas
Contains XML schema documents (`.xsd`), for validating XML files against the documentation.

The XML Schemas were generating with `trang -I xml -O xsd /path/to/xml/files/*.xml schemas/schemaName.xsd`.
They were then processed with `refRemover.py` unnecessary references to xs:elements that trang creates.

### utils
This folder contains utitlities written to help automate the early task of processing all of the game XML files.
They will likely not be needed as the processing has already been done, but may prove useful in the future for
documenting other Giants Software games. Further details are found in the utils folder readme.

## Helping Out
To help out with the documentation in any way, please read [CONTRIBUTING.md](CONTRIBUTING.md) first,
as it outlines steps that should be taken.

## Using schemas
The schema files are intended to help modders validate the configuration files in their mods. How they are used is up to
individual modders, but some suggestions can be found below.

### Referencing schema in XML file
Because this project is hosted on GitHub, schema files can be used without having to download them. Simply append these
two attributes to the top level element in the XML file to be validated (such as `<placeable>` or `<vehicle>`):

<code>
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/Marsfan/Farming-Simulator-Mod-Doc/master/schemas/<i>version</i>/<i>schema.xsd</i>"
</code>

Replacing *version* with the version of Farming Simulator that is in use (e.g `FS2019`)
and *schema.xsd* with the schema files that are desired (e.g. `placeable.xsd`)

For example, if writing an XML file for a placeable to be added to Farming Simulator 2019, the first line should be:

`<placeable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:noNamespaceSchemaLocation=
"https://raw.githubusercontent.com/Marsfan/Farming-Simulator-Mod-Doc/master/schemas/FS2019/placeable.xsd">`

Some editors (such as Visual Studio Code with the Red Hat XML extension), will use this to automatically validate the
file against the schema.

### Using an online tool
A number of tools are available to validate files against a schema. Websites can be found simply by searching for
"online xsd validator"

### Using an command line tool
On Linux, the command line tool `xmllint` can be used to quickly validate multiple XML files against a schema.
As an example, to validate all files in the current directory against a schema file in the current directory, do
`xmllint --noout --schema schema.xsd *.xml`. In the utils folder there is a tool called `validateXML.sh` that
abstracts away the flags, to simplify the process.

_Note: `xmllint` does not seem to work with fetching XML schemas from GitHub. If you wish to validate a file against
schemas with `xmllint`, you must manually download the schema and all its imports first.

### Your preferred editor/tool
If you already have a tool that you prefer for validating XML files, go ahead and use it, and add it to this readme
so that others can learn abou it.
