@Echo OFF
@Echo Launch dir: "%~dp0"
dir "%~dp0" /b
TIMEOUT 10
REM dir /b /a-d, b list files, a-d exclude directory