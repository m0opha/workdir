import  os

from ..vars.paths import _CONFIG_FILE_PATH, _CONFIG_PATH
from .colors_prompt import *

def configDirectory():
    if not os.path.exists(_CONFIG_PATH):
        os.mkdir(_CONFIG_PATH)
        pWarning("[!] Config directory has been created.")                              

    if not os.path.exists(_CONFIG_FILE_PATH):
        with open(_CONFIG_FILE_PATH, "w") as f:
            f.write("")
            pWarning("[!] Config file create.")
