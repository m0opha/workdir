from ..vars.paths import _CONFIG_FILE_PATH
from .colors_prompt import *

def unsetWorkdir():
    with open(_CONFIG_FILE_PATH, "w") as f:
        f.write("")
        
    pWarning("[!] Unset saved work path.")