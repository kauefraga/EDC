:: https://github.com/kauefraga/EDC
:: BE AWARE OF YOUR ACTIONS!

@echo off
color 2
cls

echo Getting IP Address...

curl -s "https://api.ipify.org?format=json" >> ..\net-logs.json
curl -s "https://api.ipify.org"

echo.
pause