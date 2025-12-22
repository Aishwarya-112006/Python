import os

# Specify the directory you want to list
directory = '/New folder'

# List the contents of the directory
try:
    # Get the list of files and directories in the specified directory
    content = os.listdir(directory)

    # Print the content of the directory
    print(f"Content of the directory '{directory}':")
    for item in content:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' was not found.")
except PermissionError:
    print(f"You do not have permission to access the directory '{directory}'.")