import os

from ..vars.paths import _CONFIG_FILE_PATH, _CONFIG_PATH
from .colors_prompt import * 

def getWorkDir(term=False):
    if not os.path.exists(_CONFIG_FILE_PATH):
        pError("[-] config file not exists!.")

    with open(_CONFIG_FILE_PATH) as f:
        work_path = f.read()

    if work_path == "":
        pWarning("[!] Work path is not set.")
        return
    
    if os.path.exists(work_path) == False:
        pWarning("[!] Work path save not exists.")
        return
    
    print(work_path)
    