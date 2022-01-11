import zipimport
import requests
from ..util import src_path, debug, Ok, Failure, Sucsess, Reset
import os

from uuid import uuid4
zipFiles = {}
def zipWebImport(url: str, moduleName: str, version: str, force:bool=False) -> object:
    data = requests.get(url)
    path = os.path.join(src_path, ".temp")
    if os.path.exists(path):

        debug(f"{Sucsess}Path Exsists! -> Skipping creation step!")
    
    else:
        path = os.path.join(src_path, ".temp")
        debug(f"{Ok}Creating the new path at {path}{Reset}")
        os.makedirs(path)

    
    path = os.path.join(path, f"{moduleName}-{version}.zip")
    if os.path.exists(path) and not force:
        debug(f"{Ok}File Already Exsists, just using the already made one! {Reset}")
    else:
        with open(path, "wb+") as file:
            # Write the byte to a zip
            file.write(data.content)
            zipFiles[moduleName] = {"NAME":moduleName, "path": path, "url": url}
    
    # Now import file!
    try:
        return zipimport.zipimporter(path)
    
    except zipimport.ZipImportError:
        debug(f'{Failure}Failed to import from the path {zipimport} {Reset}')
 
    
def deleteZipFiles():
    for zip in zipFiles:
        debug(f"{Ok}Removing {zip['NAME']} from {zip['path']}{Reset}")
        os.remove(zip["path"])

        