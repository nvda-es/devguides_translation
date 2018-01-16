@echo off
echo Generating application translation strings...
for %%i in (..\python_docs\*.py) do (
python pygettext.py -v -d ..\potfiles\%%~ni ..\python_docs\%%~ni.py
)