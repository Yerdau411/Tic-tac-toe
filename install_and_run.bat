@echo off
echo ========================================
echo Tic Tac Toe Game Setup
echo ========================================
echo.

echo Checking if Python is installed...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python is already installed!
    echo.
    echo Starting the game...
    python tic_tac_toe.py
    goto :end
)

echo Python is not installed or not in PATH.
echo.
echo Please follow these steps to install Python:
echo.
echo 1. Go to https://www.python.org/downloads/
echo 2. Click "Download Python" (latest version)
echo 3. Run the installer
echo 4. IMPORTANT: Check "Add Python to PATH" during installation
echo 5. Complete the installation
echo 6. Close and reopen this command prompt
echo 7. Run this batch file again
echo.
echo After installing Python, you can run the game with:
echo python tic_tac_toe.py
echo.
pause

:end 