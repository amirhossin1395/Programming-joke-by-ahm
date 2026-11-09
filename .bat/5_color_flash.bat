@echo off
:loop
color 0C
ping 127.0.0.1 -n 1 >nul
color 0A
ping 127.0.0.1 -n 1 >nul
color 0E
ping 127.0.0.1 -n 1 >nul
goto loop