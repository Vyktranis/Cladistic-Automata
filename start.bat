@echo off

rem Check if python is installed
python --version 3>NUL
if errorlevel 1 (
    echo Python 3.9 Required

    cmd /k
) else (

    rem Check if requirements.txt is there
    if exist %0\..\requirements.txt (

        rem Create Virtual Environment
        python -m venv %0\..\

        rem Enter Virtual Env
        call %0\..\Scripts\activate.bat

        rem Install Required
        pip install -r requirements.txt

        rem Delete Requirements
        del %0\..\requirements.txt
    )

    rem Run Bot
    %0\..\Scripts\python.exe %0\..\Main.py
)

