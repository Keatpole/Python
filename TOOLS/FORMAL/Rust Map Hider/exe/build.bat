@echo off

python --version > NUL
if errorlevel 1 goto NOPYTHON
goto BEGIN

:NOPYTHON
echo Python was not detected
pause >NUL

:BEGIN
cd %0\..\
pip install pyinstaller
pyinstaller --onefile "../Rust Map Hider.py" --icon "Rust Map Hider.ico"
cd dist
move "Rust Map Hider.exe" ../..
cd ..
rmdir /S /Q dist
rmdir /S /Q __pycache__
del "Rust Map Hider.spec"
cd ..
rmdir /S /Q __pycache__