import sys
import argparse
import os

from .modules import *

def main():
    configDirectory()

    parser = argparse.ArgumentParser(
        description="change directory to the work path.")

    parser.add_argument('--set', '-s', nargs='?', const=True, help="Set the work directory path. If no path is given, enables set mode.")
    parser.add_argument('--unset', '-us', action='store_true', help="Unset the current work directory.")
    parser.add_argument('--get', '-g', action='store_true', help="Show the current work directory.")
    parser.add_argument('--install-bash-script', '-ibs', action='store_true', help="Install bash helper function")
    parser.add_argument('--remove-bash-script', '-rbs', action='store_true', help="Remove bash helper function.")
    args = parser.parse_args()

    if len(sys.argv) == 1:
        getWorkDir()
        return
    

    if isinstance(args.set,str):
        if os.path.exists(args.set):
            target_path = args.set
            if target_path[0] == ".":
                target_path = os.path.abspath(target_path)

            setWorkDir(work_path=target_path)
            return
        
        pWarning("[!] Directory not exists.")
        return
    
    if args.set:
        setWorkDir()
        return

    if args.unset:
        unsetWorkdir()
        return

    if args.get:
        getWorkDir()
        return
    
    if args.install_bash_script:
        installBashScript()
        return

    if args.remove_bash_script:
        removeBashScript()
        return