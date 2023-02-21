import subprocess

displays = subprocess.run(["displayplacer", "list"], capture_output=True, text=True).stdout
displays_list = displays.strip().split("\n")

display_data = {}

for display in displays_list:
    display_info = display.split()
    origin = display_info[1]
    resolution = display_info[3]
    display_data[display_info[0]] = {"origin": origin, "resolution": resolution}

print(display_data)