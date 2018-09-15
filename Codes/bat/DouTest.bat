@echo off

title 《逗比测试程序》
color 1a
echo 你是逗比吗？
echo.
set /p var= 请输入Y或者N   -----  
echo.
if %var% == Y ( 
echo 原来你是逗比 正在注销 按任意键...
ping 127.0.0.1
shutdown -s
) else ( 
echo 你真的是逗比！
echo.
echo 遇到逗比 正在重新启动 按任意键...
pause>nul
shutdown -r
)
exit