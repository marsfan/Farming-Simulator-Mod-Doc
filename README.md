# FS2019-Mod-Doc
Documentation on everything to do with modding Farming Simulator.

This project aims to eventually have complete documentation of all of XML elements used for modding Farming Simulator 2019. \
Stretch goals include adding documentation for all prior version of Farming Simulator, and adding documentation regarding other parts of modding Farming Simulator (textures, animations, lua, etc)

# Repository Structure

## .github
The `.github` folder contains configuration files for hosting this project on GitHub.\
It contains the code of conduct file ([`CODE_OF_CONDUCT.md`](./.github/CODE_OF_CONDUCT.md)), as well as the pull request template ([`pull_request_template.md`](.github/pull_request_template.md))

Additionally, it contains teh following folders:

### ISSUE_TEMPLATE
Contains templates for issues  in github

### workflows
Contains yaml files for defineing GitHub Actions

## docs
Contains the `rst` files that define the entire documentation site, as well as the configuration files for Sphinx (the documentation generation framework)

# schemas
Contains XML schema documents (`.xsd`), for validating your xml files against the documentation.

The XML Schemas were generating with `trang -I xml -O xsd /path/to/xml/files/*.xml schemas/schemaName.xsd`. They were then manually edited to remove the large number of unnecessary references to xs:elements.