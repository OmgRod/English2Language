@echo off
setlocal

:: Function to check if Python is available and valid
:check_python
echo Checking for Python in environment variables...

:: Try to run python --version and capture the output
for /f "delims=" %%i in ('python --version 2^>nul') do set PYTHON_VERSION=%%i

if defined PYTHON_VERSION (
    echo Detected Python version: %PYTHON_VERSION%
    echo %PYTHON_VERSION% | findstr /c:"Python 3.12" >nul
    if %errorlevel% equ 0 (
        echo Python 3.7 or higher is installed.
        goto install_requirements
    ) else (
        echo Python version is not 3.7 or higher.
    )
) else (
    echo Python is not installed or not in the PATH.
)

:: Ask user if they want to open the Microsoft Store page for Python 3.12
set /p userInput="Do you want to open the Microsoft Store page for Python 3.12? (Y/N): "
if /i "%userInput%"=="Y" (
    echo Opening Microsoft Store page for Python 3.12...
    
    :: Open the URL
    start "" "ms-windows-store://pdp/?productid=9NCVDN91XZQP"
    
    :: Optionally, you can exit after opening the store page
    goto end
) else (
    echo Python is not installed. Please install Python manually.
    pause
)

:install_requirements
if exist requirements.txt (
    echo Installing packages from requirements.txt...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found.
)

:end
echo Exiting...
endlocal
exit /b