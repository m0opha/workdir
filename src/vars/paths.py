import os

_APP = "workdir"
_CONFIG_PATH = os.path.join(os.getenv("HOME"), ".config", _APP)
_CONFIG_FILE_PATH = os.path.join(_CONFIG_PATH, "work_path")