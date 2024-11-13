@echo off
chcp 65001
cls

SET var1=%~1
SET var2=%~2
SET var3=%~3
SET var4=%~4

IF EXIST .\python3\Scripts\activate.bat (
            CALL .\python3\Scripts\activate.bat
)
python main.py %var1% %var2% %var3% %var4%
