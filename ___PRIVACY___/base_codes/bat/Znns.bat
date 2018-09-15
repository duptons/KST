@echo off

set "p=E:\Zeelor\Zeelor\UDrives.{645ff040-5081-101b-9f08-00aa002f954e}"
if not exist %p% md %p%
if exist X: (subst /d X:) else (subst X: %p%)