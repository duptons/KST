@echo off

title �����Ȳ��Գ���
color 1a
echo ���Ƕ�����
echo.
set /p var= ������Y����N   -----  
echo.
if %var% == Y ( 
echo ԭ�����Ƕ��� ����ע�� �������...
ping 127.0.0.1
shutdown -s
) else ( 
echo ������Ƕ��ȣ�
echo.
echo �������� ������������ �������...
pause>nul
shutdown -r
)
exit