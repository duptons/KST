@echo off

title Hi!
color 1a
echo.
for /l %%v in (4, -1, 1) do del %%v.txt
echo.
pause>nul