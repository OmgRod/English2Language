@echo off
setlocal

:: Check for existing Python installation
where python >nul 2>nul
if %errorlevel% equ 0 (
    :: Python is installed, proceed with pip install
    echo Python is already installed.
    if exist requirements.txt (
        echo Installing packages from requirements.txt...
        pip install -r requirements.txt
    ) else (
        echo requirements.txt not found.
    )
    goto end
)

:: Python is not installed, ask user if they want to install Python 3.11
set /p userInput="Do you want to install Python 3.11? (Y/N): "
if /i "%userInput%"=="Y" (
    echo Downloading and installing Python 3.11...
    
    :: Set the URL for Python 3.11 installer
    set "url=https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe"
    set "installer=python-3.11.0-amd64.exe"
    
    :: Download the installer
    powershell -Command "Invoke-WebRequest -Uri %url% -OutFile %installer%"
    
    :: Run the installer silently
    start /wait %installer% /quiet InstallAllUsers=1 PrependPath=1
    
    :: Clean up the installer file
    del %installer%
    
    :: Check if Python is installed
    where python >nul 2>nul
    if %errorlevel% equ 0 (
        echo Python 3.11 has been installed successfully.
        if exist requirements.txt (
            echo Installing packages from requirements.txt...
            pip install -r requirements.txt
        ) else (
            echo requirements.txt not found.
        )
    ) else (
        echo Python installation failed. Please install Python manually.
    )
) else (
    echo Python is not installed. Please install Python manually.
    pause
)

:end
echo Exiting...
endlocal
exit /b