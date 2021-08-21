@echo off

if exist %0\..\requirements.txt (

    python -m venv %0\..\

    call %0\..\Scripts\activate.bat

    pip install -r requirements.txt

    del %0\..\requirements.txt
)

%0\..\Scripts\python.exe %0\..\Main.py