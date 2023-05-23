import os

def find_vulnerable_executables():
  # Use the find command to get a list of all executables on the system
  output = os.popen("find / -perm -u=x -type f").read()

  # Loop through the list of executables and check their dynamic library load commands
  for line in output.split("\n"):
    # Skip empty lines
    if not line:
      continue

    # Use the otool command to get the list of dynamic libraries that are loaded by the executable
    libraries = os.popen(f"otool -L {line}").read()

    # Check if the executable has any dynamic library load commands
    if "@rpath" in libraries or "/usr/local/lib" in libraries:
      print(line)

# Example usage
find_vulnerable_executables()
