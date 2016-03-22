@echo off

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

echo ===============================
%PPYTHON_PATH% -m  prepare_client
echo ===============================

pause
