# DisplayOriginSwap (dos)
## Swaps the position of two displays using the displayplacer command line utility.
Provides a workaround to the issue where Macs will randomly reverse the screen arrangement of identical external displays.  
Runs 'displayplacer list' to extract current screen configuration.  
Runs 'displayplacer' with the correct arguments to swap the origin position of two displays.

### Displayplacer
https://github.com/jakehilborn/displayplacer  
  macOS command line utility to configure multi-display resolutions and arrangements.  
Install via Homebrew with:
```
    brew tap jakehilborn/jakehilborn && brew install displayplacer
```
### Alias
You may want to alias this script for ease of execution. Typing 'dos' in the shell will execute this script.
The example below will need to be modified for your environment and appended to your .bash_profile or .zshrc.
```
alias dos='/Users/kernelpanic/.pyenv/versions/3.9.1/bin/python /Users/kernelpanic/vscode/dos/dos.py'
```
