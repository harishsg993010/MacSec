import os

def find_priviledged_xpc_services():
  # Use the launchctl command to get a list of all loaded services
  output = os.popen("launchctl list").read()

  # Loop through the list of services and check their privileges
  for line in output.split("\n"):
    # Split the line into columns
    columns = line.split()
    # Check if the service has the "root" privilege
    if len(columns) >= 3 and columns[2] == "root":
      # Use the find command to search for the executable of the privileged service
      path = os.popen(f"find / -name {columns[0]}").read().strip()
      print(path)

# Example usage
find_priviledged_xpc_services()
