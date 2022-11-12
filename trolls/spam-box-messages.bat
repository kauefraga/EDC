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
cls
color 2

set /A numberOfBoxes=10

echo msgbox "Something went wrong",16, ":((" > msg.vbs
echo for /l %%%%r in ^(1,1,%numberOfBoxes%^) do ^(start msg.vbs^) > runner.cmd
echo exit >> runner.cmd
start /separate runner.cmd > nul
