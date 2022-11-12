#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/my-dotfiles

function Print {
  param (
    [string] $message,
    [string] $color = 'green'
  )
  Write-Host '[Ana]' $message -ForegroundColor $color
}

function Input {
  param (
    [string] $message
  )
  Print $message

  $value = Read-Host '>>>'

  return $value
}

Clear-Host

# "`n" escape character
Write-Host '*****************************************' -ForegroundColor 'magenta'
Write-Host '*    Relax! Ana will take control...    *' -ForegroundColor 'magenta'
Write-Host '*****************************************'"`n" -ForegroundColor 'magenta'

if (-Not (Test-Path "$env:userprofile/scoop"))
{
  Print 'installing scoop...'
  Set-ExecutionPolicy RemoteSigned -Scope CurrentUser # Optional: Needed to run a remote script the first time
  Invoke-RestMethod 'get.scoop.sh' | Invoke-Expression # irm get.scoop.sh | iex
  Print 'scoop is now available'
}

$packages = @(
  'git', 'docker', 'docker-compose', 'fnm', 'pwsh', 'virtualbox-with-extension-pack-np',
  'go', 'python', 'mingw', 'alacritty'
  'winrar-np',
  'min',
  'JetBrains-Mono'
)

Print 'installing packages...'
ForEach ($package in $packages)
{
  # add buckets (extra, games, nonportable, nerd-fonts...) before
  scoop install $packages
}
Print 'done'

Print 'configuring git...'
git config --global core.autocrlf false

$username = Input 'Whats your git username? '
$email = Input 'Whats your git email? '

git config --global user.name $username
git config --global user.email $email
Print 'done'

Print 'configuring nodejs...'
fnm env --use-on-cd | Out-String | Invoke-Expression
fnm install --lts
fnm use lts-latest
Print 'done'

Print 'if you wanna spotify, look at this https://github.com/SpotX-CLI/SpotX-Win'

Print 'byebye <3'
