@echo off

python -m venv %0\..\

call %0\..\Scripts\activate.bat

pip install -r requirements.txt
