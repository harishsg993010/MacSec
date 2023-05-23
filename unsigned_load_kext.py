import os

def find_vulnerable_executables():
  # Use the kextstat command to get a list of all loaded kernel extensions
  output = os.popen("kextstat").read()

  # Loop through the list of kernel extensions and check if any of them are unsigned
  for line in output.split("\n"):
    # Split the line into columns
    columns = line.split()
    # Check if the kernel extension is unsigned
    if len(columns) >= 6 and columns[5] == "(unsigned)":
      # The name of the executable that loaded the unsigned kernel extension will be in the fourth column
      print(columns[3])

# Example usage
find_vulnerable_executables()
