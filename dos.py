""" DisplayOriginSwap (dos)

Swaps the position of two displays using the displayplacer command line utility.
Provides a workaround to the issue where Macs will randomly reverse the screen arrangement of identical external displays.
Runs 'displayplacer list' to extract current screen configuration.
Runs 'displayplacer' with the correct arguments to swap the origin position of two displays.

https://github.com/jakehilborn/displayplacer
macOS command line utility to configure multi-display resolutions and arrangements.
Install via Homebrew with:
brew tap jakehilborn/jakehilborn && brew install displayplacer

You may want to alias this for ease of execution. Typing 'dos' in the shell will execute this script.
The example below will need to be modified for your environment and appended to your .bash_profile or .zshrc.
alias dos='/Users/kernelpanic/.pyenv/versions/3.9.1/bin/python /Users/kernelpanic/vscode/dos/dos.py'    
"""

import subprocess

# Create lists to store extracted displayplacer data
screen_id = []
resolution = []
origin = []

# Create vars to define the displays to swap.
# The values should reflect the order they appear in the 'displayplacer' list command.
# First appearance is 0, second is 1, etc.
# If you have two external displays with the built-in display as the main display, the defaults should work.
display1 = 1
display2 = 2

# Run the "displayplacer list" command and split it into lines
output = subprocess.run(["displayplacer", "list"], capture_output=True).stdout.decode()
lines = output.strip().split("\n")

# Find lines that contain either the id, resolution or origin, and split at the colon.
# Append the data to the lists created earlier.
for line in lines:
    if "Persistent screen id:" in line:
        screen_id.append(line.split(":")[1].strip())

    if "Resolution:" in line:
        resolution.append(line.split(":")[1].strip())

    if "Origin:" in line:
        origin.append(line.split(":")[1].strip())

# Build the displayplacer command arguments for each display.  The origin is swapped for each display.
display1_argument = (f"id:{screen_id[display1]} resolution:{resolution[display1]} origin:{origin[display2]}")
display2_argument = (f"id:{screen_id[display2]} resolution:{resolution[display2]} origin:{origin[display1]}")

# Print the display info including the current and new origins for the two displays that will swap position. 
print(f"id:{screen_id[1]} resolution:{resolution[display1]} \t current origin:{origin[display1]} \t new origin:{origin[display2]}")
print(f"id:{screen_id[2]} resolution:{resolution[display2]} \t current origin:{origin[display2]} \t new origin:{origin[display1]}")

# Print the displayplacer command that will run so it can be copied if desired.
# This appends double quotes which are not used when calling via subprocess.run.
print(f"\ndisplayplacer \"{display1_argument}\" \"{display2_argument}\"")

# Run the "displayplacer" command with arguments that swap the origin of the two displays.
# Check the return status code and create an exception if not 0.
output = subprocess.run(["displayplacer", display1_argument, display2_argument], check=True, capture_output=True).stdout.decode()

# Print subprocess output (none expected)
print(output)