@echo off

set "p=E:\Zeelor\Zeelor\UDrives.{645ff040-5081-101b-9f08-00aa002f954e}"

:: 下面是块注释
goto start
set "p=E:\Zeelor\C\T.{645ff040-5081-101b-9f08-00aa002f954e}"
:start

if not exist %p% md %p%
if exist X: (subst /d X:) else (subst X: %p%)
