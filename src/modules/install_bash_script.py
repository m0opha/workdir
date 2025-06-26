
import os
import re
import subprocess

from .colors_prompt import *

TARGET_SCRIPT_PATH = "./scripts/bash_change_dir.sh"
TARGET_FUN = "workdir"
BASHRC_PATH = os.path.expanduser("~/.bashrc")

def isBashFunctionPresent():
    if not os.path.exists(BASHRC_PATH):
        return False

    with open(BASHRC_PATH, "r") as f:
        lines = f.readlines()

    pattern = re.compile(rf'^\s*(function\s+)?{re.escape(TARGET_FUN)}\s*\(\)?\s*\{{\s*$')

    for line in lines:
        if pattern.match(line):
            return True

    return False

def installBashScript():
    if isBashFunctionPresent():
        pWarning("[!] Bash scritp already installed.")
        return
    
    command = f"cat {os.path.abspath(TARGET_SCRIPT_PATH)} >> {BASHRC_PATH}"
    result = subprocess.run(
        command, 
        capture_output=True,
        #text=True,
        #shell=True
        )
    if result.returncode == 0:
        pSuccess("[+] Bash script helper installed.")
        return
    pError("[-] Bash script not installed")

if __name__ == "__main__":
    installBashScript()
