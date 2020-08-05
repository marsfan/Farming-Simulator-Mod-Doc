# How to Contribute

## Code of Conduct
The Code of Conduct can be found in this repository, under the path .github/CODE_OF_CONDUCT.md.

THIS MUST BE FOLLOWED, NO EXCEPTIONS.

## Reporting problems
If you experience any sort of problem, first check if anyone else has already reported the same issue.
If not, open an issue and detail exactly what problem you are having.\
There are a number of template styles for filing issues, pick the one that fits your issue best, and fill out the
sections\
If a section in the template is not needed for your issue, feel free to leave it out.\

## Submitting Pull Requests
Before starting on work, check the existing issues and pull requests to make sure someone else is not already
working on the same thing.\
Pull requests descriptions will automatically populate with template with sections to fill out regarding the pull
request.\
If a section in the template is unneeded for your pull request, feel free to leave it out.

## Proof
When submitting issues or pull requets that will change the documentation, you must have an example that proves
that your change is correct. Do not make up your own example, instead, find one that is known to work in the game.
This could be:
* A configuration file in the game.
* A configuration file in a mod.
* Information from a reliable source.

Do not copy and paste the proof into your Pull Request or Issue. We do not want to risk being accused of allowing
people to share private or proprietary information. Instead, describe where the example can be found.
This could either be by providing the filepath that the example can be found on a users computer, or a link to where
the example file can be downloaded (GitHub, ModHub, or any other modding site). Submissions that do paste in example
code from another source will have it edited to be removed, and asked to instead provide a link to relavent information.

## Helping out with documentation
If you do not understand how GitHub works, or how to properly edit the documentation, but you want to contribute, you
can create an issue. Be sure to carefully document what you would change, why you would change it, and provide some
evidence to prove why the change is necessary. If you propose a change through this method, it may take a little
while to add your suggestion.

If, on the other hand, you do understand GitHub, please fork the repository, make your changes, and file a pull request.

Please look through the list of open issues, to add something that someone else may have suggested. If you see something
that you would like to assign to yourself, add a comment to the issue stating that you would like to take resonsibility
for the suggestion.

Anther way to find things that need to be worked on is to look at the Documentation TODOs page in the documentation.
It lists every time that a `.. todo::` directive is used in the documentation.

If you can partially improve something in the documentation, add a `.. todo::` directive to it afterwards, to flag it as
needing work, so that other contributers can quickly find things to help out with.

## Python Config
The actual documentation pages are built using [Sphinx](https://www.sphinx-doc.org/en/master/), which is written in
[Python](https://www.python.org/). As such, it (and extensions used in the project), are installed using pip.

If you want to test your changes to the documentation yourself, or plan to experiment with modifications to the
documentation configuration, you will need to install Python, and then install the project requirements specified in
 `docs/requirements.txt` with pip. This can be done with the command  `pip install -U -r requirements.txt`. I advise using a
Python virtual environment (such as [venv](https://docs.python.org/3/library/venv.html)) to keep this projects
requirements from breaking other projects you might have. Note that Python virtual environments are not complete
virtual machines (like VirtualBox), but simply a special folder structure to keep each project's requirements seperate

The same applies for if you want to modify/experiment with scriptsin the utils folder. In that folder is a requirements
file with all of the requirements for the utilities.

### Testing Schemas
If you want to test modifications you have made to a schema document (one that ends in `.xsd`), you will have to modify
an xml file to properly reference the schema file. An example below is for a xml file for a placeable object.

In the `<placeable>` xml tag at the beginning of the file, add these two options:

`xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="path_to_schemas/placeables.xsd"`

This results in the tag now looking like:

`<placeable xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="placeables.xsd">`

An alternative method to validating schema files is to use a seperate utitlity for checking files, such as `xmllint`

