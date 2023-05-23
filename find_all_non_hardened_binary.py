import os

def find_non_hardened_binaries():
  # Use the find command to get a list of all executables on the system
  output = os.popen("find / -perm -u=x -type f").read()

  # Loop through the list of executables and check their code signing status
  for line in output.split("\n"):
    # Skip empty lines
    if not line:
      continue

    # Use the codesign command to check the code signing status of the executable
    status = os.popen(f"codesign -dvvv {line}").read()

    # Check if the executable is not signed or is signed with an ad-hoc signature
    if "not signed" in status or "ad-hoc" in status:
      print(line)

# Example usage
find_non_hardened_binaries()
