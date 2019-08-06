@echo off
echo Generating application translation strings...
for %%i in (..\python_docs\*.py) do (
xgettext -o ..\potfiles\%%~ni.pot ..\python_docs\%%~ni.py
)