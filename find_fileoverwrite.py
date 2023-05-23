import os

def find_file_overwrite_vulnerabilities():
  # Use the ls command to get a list of all files on the system
  output = os.popen("ls -lO /").read()

  # Loop through the list of files and check their flags
  for line in output.split("\n"):
    # Split the line into columns
    columns = line.split()
    # Check if the file has the "schg" flag
    if len(columns) >= 10 and "schg" not in columns[5]:
      print(columns[8])

# Example usage
find_file_overwrite_vulnerabilities()