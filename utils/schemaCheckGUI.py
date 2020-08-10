"""Simple GUI Application to validate XML files that are sorted by xmlTypeSorter.py against repo schemas."""

import xmlschema
from typing import Dict, List
from pathlib import Path
import tkinter as tk
import tkinter.ttk as ttk

schemaDir = Path("./schemas/FS2019")
xmlDirs = Path("./utils/sortedXML")


class GUI(tk.Tk):


    def __init__(self):
        super().__init__()

        self.errors: Dict[str, Dict[str, List[Exception]]] = {}


        self.startButton = ttk.Button(self, text="start", command=lambda: self.after(1, self.parseFiles))
        self.schemaSelect = ttk.Combobox(self, values=[])
        self.xmlSelect = ttk.Combobox(self, value=[])

        self.startButton.grid(row=0, column=0)
        self.schemaSelect.grid(row=1, column=0)
        self.xmlSelect.grid(row=2, column=0)


    def parseFiles(self):
        for schemaFile in schemaDir.glob("*.xsd"):
            schema = xmlschema.XMLSchema(str(schemaFile))
            for file in xmlDirs.joinpath(schemaFile.stem).glob("*.xml"):
                if not schema.is_valid(str(file)):
                    try:
                        schema.validate(str(file))
                    except xmlschema.XMLSchemaChildrenValidationError as ex:
                        try:
                            self.errors[str(schemaFile)][str(file)]
                        except KeyError:
                            try:
                                self.errors[str(schemaFile)][str(file)] = []
                            except KeyError:
                                self.errors[str(schemaFile)] = {}
                                self.errors[str(schemaFile)][str(file)] = []

                        finally:
                            self.errors[str(schemaFile)][str(file)].append(ex)
        self.schemaSelect.values = list(self.errors.keys())


if __name__ == "__main__":
    ui = GUI()
    ui.mainloop()
