from .core import webImport, zipWebImport


import os
from .util import src_path, debug, Ok, Failure, Sucsess, Reset
from .core import deleteZipFiles


class program():
    def __init__(self) -> None:
        # Create the Temp File
        if os.path.exists(os.path.join(src_path, ".temp")):
            debug(f"{Sucsess}Path Exsists! -> Skipping creation step!")

        else:
            path = os.path.join(src_path, ".temp")
            debug(f"{Ok}Creating the new path at {path}{Reset}")
            os.makedirs(path)

    # At any interupt or end of file the python interpreter will call this
    def __del__(self): # No more dameons
        # All Classes 
        deleteZipFiles() # Remove Temp

