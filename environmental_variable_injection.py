import os

def find_executables_with_entitlement():
  # Use the find command to get a list of all executables on the system
  output = os.popen("find / -perm -u=x -type f").read()

  # Loop through the list of executables and check their entitlements
  for line in output.split("\n"):
    # Skip empty lines
    if not line:
      continue

    # Use the codesign command to get the entitlements of the executable
    entitlements = os.popen(f"codesign -d --entitlements - {line}").read()

    # Check if the executable has the com.apple.security.cs.allow-dyld-environment-variables entitlement
    if "com.apple.security.cs.allow-dyld-environment-variables" in entitlements:
      print(line)

# Example usage
find_executables_with_entitlement()
