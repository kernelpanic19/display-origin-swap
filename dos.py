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
alias dos='python ~/Code/dos/dos.py'    
"""

import subprocess
import sys

def get_display_list():

    # Create a list to store extracted displayplacer data as dictionaries
    display_data = []

    # Run the "displayplacer list" command and split it into lines
    output = subprocess.run(["displayplacer", "list"], capture_output=True).stdout.decode()
    lines = output.strip().split("\n")

    # Temporary dictionary to store data for each display
    current_display_data = {}

    print("Detected screens:")
    # Find lines that contain either the id, resolution or origin, and split at the colon.
    # Append the data to the dictionaries and add them to the display_data list.

    for line in lines:
        if "Persistent screen id:" in line:
            current_display_data["screen_id"] = line.split(":")[1].strip()
        
        if "Type:" in line:
            current_display_data["type"] = line.split(":")[1].strip()

        if "Resolution:" in line:
            current_display_data["resolution"] = line.split(":")[1].strip()

        if "Origin:" in line:
            current_display_data["origin"] = line.split(":")[1].strip()
            display_data.append(current_display_data)
            screen_index = display_data.index(current_display_data)
            print(f"screen {screen_index}: {current_display_data}")
            current_display_data = {}
    return(display_data)

def validate_inputs(displays_to_swap, display_data):
    # Check if the display indexes in displays_to_swap are within the range of available displays.
    if any(d >= len(display_data) for d in displays_to_swap):
        print("Error: One or more display indexes in displays_to_swap do not reference a detected screen.")
        sys.exit(1)

def print_display_info(displays_to_swap, display_data):
    print("\nSwapping display origin of screens:")
    for i, d in enumerate(displays_to_swap):
        print(f"screen {d}: type:{display_data[d]['type']} resolution:{display_data[d]['resolution']} \t current origin:{display_data[d]['origin']} \t new origin:{display_data[displays_to_swap[1 - i]]['origin']}")

def swap_displays(displays_to_swap, display_data):
    displayplacer_arguments = [
        f"id:{display_data[d]['screen_id']} resolution:{display_data[d]['resolution']} origin:{display_data[displays_to_swap[1 - i]]['origin']}"
        for i, d in enumerate(displays_to_swap)
    ]

    print("\nExecuting:")
    print(f"displayplacer \"{displayplacer_arguments[0]}\" \"{displayplacer_arguments[1]}\"")

    output = subprocess.run(["displayplacer", displayplacer_arguments[0], displayplacer_arguments[1]], check=True, capture_output=True).stdout.decode()

    print(output)

def main():
    displays_to_swap = (1, 2)
    display_data = get_display_list()

    validate_inputs(displays_to_swap, display_data)
    print_display_info(displays_to_swap, display_data)
    swap_displays(displays_to_swap, display_data)

if __name__ == "__main__":
    main()