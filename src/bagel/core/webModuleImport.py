import requests
import zipimport
from ..util import debug, Ok, Sucsess, Reset, Failure



def webModuleImport(URL:str):
    # Must be Zip Imported

    try:
        zipimport.zipimporter(archivepath)
    except zipimport.ZipImportError():
        debug(f"{Failure}While Import Zip file, it couldn't find it{Sucsess}")

        