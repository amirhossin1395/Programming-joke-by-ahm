@echo off
:loop
start cmd /c "echo HACKED! & timeout /t 1 >nul"
timeout /t 0 /nobreak >nul
goto loop