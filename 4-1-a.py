import os

# List files in the current directory of the Python program
os.listdir(path='.') 
  
# Assign a directory path to a string
directory =  "C:\\test"

# Check if directory provided exists on file system
# Returns True if exists
print(os.path.exists(directory))

# List files in the directory provided if exists[C:\test]
if os.path.exists(directory):
    print(os.listdir(path=directory))

# Make the directory if does not exist
if not os.path.exists(directory):
    os.makedirs(directory)
