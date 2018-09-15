@echo off

md F:\U-pan\tools\UnDriver.{645ff040-5081-101b-9f08-00aa002f954e} > nul
if exist Y:\nul goto delete
subst Y: F:\U-pan\tools\UnDriver.{645ff040-5081-101b-9f08-00aa002f954e}
goto end
:delete
subst /d Y:
:end
