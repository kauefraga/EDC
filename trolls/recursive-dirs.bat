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

set /A n=0

echo Loop will start now
:init
mkdir folder%n%
cd folder%n%

set /A n+=1
goto init
