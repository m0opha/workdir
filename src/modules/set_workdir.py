import os

from ..vars.paths import _CONFIG_FILE_PATH, _CONFIG_PATH
from .colors_prompt import *

def setWorkDir(work_path=""):

    if work_path == "":
        work_path =  os.getenv("PWD")

    with open(_CONFIG_FILE_PATH, "w") as file:
        file.write(work_path)
        pSuccess("[+] Work directory set.")
        return True
    
    return None