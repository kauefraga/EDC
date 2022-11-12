#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/edc
# BE AWARE OF YOUR ACTIONS!

function Print {
  param (
    [string] $message,
    [string] $color = 'green'
  )
  Write-Host '[Ana]' $message -ForegroundColor $color
}

Clear-Host

Print "Getting IP Address..."

$res = irm "https://api.ipify.org?format=json"

Print $res.ip
