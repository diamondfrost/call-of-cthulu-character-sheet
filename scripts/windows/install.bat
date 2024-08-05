@echo Off

Set "VIRTUAL_ENV=coc-sheet-env"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    pip install virtualenv
    python -m venv %VIRTUAL_ENV%
)

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" Exit /B 1

Call "%VIRTUAL_ENV%\Scripts\activate.bat"
pip install -r requirements.txt
