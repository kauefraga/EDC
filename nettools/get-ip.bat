::   /$$   /$$ /$$$$$$$$
::  | $$  /$$/| $$_____/
::  | $$ /$$/ | $$
::  | $$$$$/  | $$$$$
::  | $$  $$  | $$__/
::  | $$\  $$ | $$
::  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
::  |__/  \__/|__/      github.com/kauefraga/edc
:: BE AWARE OF YOUR ACTIONS!

@echo off
color 2
cls

echo [ana] Getting IP Address...

curl -s "https://api.ipify.org?format=json" >> ..\net-logs.json
curl -s "https://api.ipify.org"

echo.
pause
