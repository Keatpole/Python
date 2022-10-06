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
pyinstaller --onefile "../HKBW.py" --icon "HKBW.ico"
cd dist
move "HKBW.exe" ../..
cd ..
rmdir /S /Q dist
rmdir /S /Q __pycache__
del "HKBW.spec"
cd ..
rmdir /S /Q __pycache__