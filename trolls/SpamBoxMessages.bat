:: https://github.com/kauefraga/EDC
:: BE AWARE OF YOUR ACTIONS!

@echo off
cls
color 2

set /A numberOfBoxes=10

echo msgbox "{{ tired dev }}",16, ":)" > script.vbs
echo for /l %%%%r in ^(1,1,%numberOfBoxes%^) do ^(start script.vbs^) > k.cmd
echo exit >> k.cmd
start /separate k.cmd > nul