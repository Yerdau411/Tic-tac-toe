@echo off
echo ========================================
echo Git Setup for GitHub Upload
echo ========================================
echo.

echo Checking if Git is installed...
git --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Git is already installed!
    echo.
    echo Starting Git setup...
    goto :setup_git
)

echo Git is not installed.
echo.
echo Please follow these steps to install Git:
echo.
echo 1. Go to https://git-scm.com/download/win
echo 2. Download Git for Windows
echo 3. Run the installer with default settings
echo 4. Complete the installation
echo 5. Close and reopen this command prompt
echo 6. Run this batch file again
echo.
echo After installing Git, we'll set up your GitHub repository.
echo.
pause
goto :end

:setup_git
echo Setting up Git repository...
git init
echo.
echo Adding files to Git...
git add .
echo.
echo Creating initial commit...
git commit -m "Initial commit: Tic Tac Toe game with Python and HTML versions"
echo.
echo Setting up remote repository...
git remote add origin https://github.com/AidenDaysGrace/Tic-tac-toe.git
echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main
echo.
echo Success! Your Tic Tac Toe game has been uploaded to GitHub.
echo Visit: https://github.com/AidenDaysGrace/Tic-tac-toe
echo.
pause

:end 