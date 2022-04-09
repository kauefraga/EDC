:: https://github.com/kauefraga/EDC
:: It's so fine!
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

