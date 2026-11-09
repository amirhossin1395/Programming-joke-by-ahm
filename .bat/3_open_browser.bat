@echo off
for /l %%x in (1, 1, 100) do (
    start chrome https://www.google.com
)