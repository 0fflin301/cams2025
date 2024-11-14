@echo off
cls
ECHO ===================================
ECHO Check Python version
ECHO ===================================
python --version 2>NUL
IF ERRORLEVEL 1 (
    SETLOCAL ENABLEDELAYEDEXPANSION
    SET "PYTHON_VERSION=3.11.9"
    SET "PYTHON_ARCH=64"
    IF "%PROCESSOR_ARCHITECTURE%"=="x86" (
        IF NOT DEFINED PROCESSOR_ARCHITEW6432 SET "PYTHON_ARCH=32"
    )
    SET "PYTHON_URL=https://www.python.org/ftp/python/!PYTHON_VERSION!/python-!PYTHON_VERSION!-amd!PYTHON_ARCH!.exe"
    ECHO !PYTHON_URL!
    SET "PYTHON_PATH=C:\python\python!PYTHON_VERSION!"
    SET "PYTHON_EXE=!PYTHON_PATH!\python.exe"
    ECHO Python is not in PATH
    ECHO ===================================
    ECHO Downloading Python !PYTHON_VERSION!...
    ECHO ===================================
    curl -o "python!PYTHON_VERSION!-installer.exe" "!PYTHON_URL!" --ssl-no-revoke
    ECHO ===================================
    ECHO Installing Python...
    ECHO ===================================
    START /wait python!PYTHON_VERSION!-installer.exe /passive InstallAllUsers=1 TargetDir="!PYTHON_PATH!" PrependPath=1 Include_pip=1 Include_launcher=1 AssociateFiles=1
    DEL ".\python!PYTHON_VERSION!-installer.exe"
    ECHO ===================================
    ECHO Python successfully installed.
    ECHO ===================================
    SET "PATH=!PYTHON_PATH!;!PYTHON_PATH!\Scripts;!PATH!"
    ECHO "PATH updated: !PATH!"  REM para verificar PATH
    !PYTHON_EXE! -m pip install --upgrade pip
    ECHO ===================================
    ECHO Initializing setup
    ECHO ===================================
    !PYTHON_EXE! setup.py !PYTHON_PATH!
    ECHO ===================================
    ECHO Configuration is complete
    ECHO ===================================
    ENDLOCAL
) ELSE (
    python -m pip install --upgrade pip
    python -m pip show streamlink >NUL 2>&1
    IF ERRORLEVEL 1 (
        ECHO ===================================
        ECHO Initializing setup
        ECHO ===================================
        python setup.py
        ECHO ===================================
        ECHO Configuration is complete
        ECHO ===================================
    ) ELSE (
        python -m pip show virtualenv >NUL 2>&1
        IF ERRORLEVEL 1 (
            ECHO Installing virtualenv...
            python -m pip install virtualenv
        ) 
        python -m virtualenv python3
        IF EXIST .\python3\Scripts\activate.bat (
            CALL .\python3\Scripts\activate.bat
            python -m pip install --upgrade pip
            ECHO ===================================
            ECHO Initializing setup
            ECHO ===================================
            python setup.py
            ECHO ===================================
            ECHO Configuration is complete
            ECHO Virtual environment activated
            ECHO Use 'deactivate' to deactivate the environment
            ECHO ===================================
        ) ELSE (
            ECHO Error: activate.bat not found.
        )
    )
)
CMD /K
