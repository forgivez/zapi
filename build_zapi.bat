@chcp 65001 >nul
@echo off
echo.
echo ================================
echo     🚀 Zapi 빌드 자동화 시작
echo ================================

:: 기존 빌드 제거
echo [정리] 기존 dist, build 제거 중...
rmdir /s /q dist
rmdir /s /q build

:: 빌드 실행
echo [빌드] PyInstaller 실행 중...
pyinstaller app.py ^
 --noconsole ^
 --onefile ^
 --name Zapi ^
 --icon=icon\zapi_icon.ico ^
 --add-data "icon\zapi_icon.ico;icon" ^
 --add-data "icon\splash_dark_small.png;icon"

echo.
echo [완료] dist\\Zapi.exe 파일이 생성되었습니다!
pause
