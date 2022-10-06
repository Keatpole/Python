@echo off

python --version > NUL
if errorlevel 1 goto NOPYTHON
goto BEGIN

:NOPYTHON
echo Python was not detected
pause >NUL
exit

:BEGIN
cd %0\..\
title Building...
pip install pyinstaller
pyinstaller --onefile "../Astroneer Lookup.py" --icon "Astroneer Icon.ico"
cd dist
move "Astroneer Lookup.exe" ../..
cd ..
rmdir /S /Q dist
rmdir /S /Q build
rmdir /S /Q __pycache__
del "Astroneer Lookup.spec"
echo The build is complete. Go to the main folder to see it. > DONE.txt
title Done!
cls
echo The build is complete. Go to the main folder to see it.
timeout /t 15
del DONE.txt