pyinstaller --onefile -i NONE handler_workdir.py
cp dist/handler_workdir ~/bin
bash ./scripts/create_bash_function.sh


