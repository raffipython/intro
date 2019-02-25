# Read a file
# Assign a variable for file name
logFileName = "test.txt"
fileContent = []

# Open the file for reading
with open(logFileName) as fd:
    f = fd.read()
	# Iterate through the lines 
    for line in f.split("\n"):
		# If line not empty add it the file content list
        if line:
            fileContent.append(line)   
# Iterate through the file content list and print each line
for line in fileContent:
    print(line)

# Write a file.
# Copy the content of the file above to a new file.
with open("COPY_" + logFileName, 'w') as fd:
    for line in fileContent:
        fd.write(line + "\n")
    fd.write("New line added to the copy\n")