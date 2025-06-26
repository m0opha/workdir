import os

from .colors_prompt import *

START_FUN = "workdir() {"
END_FUN = "}"
TARGET_FUN = "workdir"

def removeBashScript():
    bashrc_path = os.path.expanduser("~/.bashrc")

    with open(bashrc_path, "r") as f:
        lines = f.readlines()

    start_at = None
    end_at = None
    inside_function = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not inside_function and stripped.startswith(f"{TARGET_FUN}()"):
            start_at = idx
            inside_function = True
            continue

        if inside_function and stripped == END_FUN:
            end_at = idx
            break

    if start_at is not None and end_at is not None:
        del lines[start_at:end_at+1]

        # Guardar los cambios
        with open(bashrc_path, "w") as f:
            f.writelines(lines)

        pSuccess(f"[-] bash script remove.")
        return
    
    pError(f"[-] bash script not found.")
    return

if __name__ == "__main__":
    removeScriptBash()