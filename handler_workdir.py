import sys
import os

__APP = "workdir"
__CONFIG_FILENAME_PREFIX = "config"
__CONFIG_PATH = os.path.join(os.getenv("HOME"), ".config", __APP)
__CONFIG_FILE_PATH = os.path.join(__CONFIG_PATH, __CONFIG_FILENAME_PREFIX)

def createConfigDirectory():
    if os.path.exists(__CONFIG_PATH) == False:
        os.mkdir(complete_path)
        print("[+]Config folder has been created")                              

def setWorkingDirectory():
    working_path =  os.getenv("PWD")
    with open(__CONFIG_FILE_PATH, "w") as file:
        file.write(working_path)
        print("[+]Working directory has been set")
    
def getWorkingDirectory():
    with open(__CONFIG_FILE_PATH) as file:
        working_path = file.read()
    if os.path.exists(working_path) == False:
        print("[-]Path saved is corrupted")
        sys.exit(1)
    print(working_path)

def main():
    createConfigDirectory()
    arg = sys.argv
    if len(arg) > 1:
        if arg[1] == "set":
            setWorkingDirectory()
            sys.exit(0)
    getWorkingDirectory()

if __name__ == "__main__":
    main()
