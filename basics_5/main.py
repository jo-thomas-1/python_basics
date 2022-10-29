# Write Python code to open a file named Fileprogram.txt and write some random data into it.

file = open("Fileprogram.txt", "w")
content = "This is test file"
file.write(content)
file.close()

# Open the file, read the contents and display them as output.

file = open("Fileprogram.txt", "r")
content = file.read()
print(content)
file.close()

# Write python code to add additional text to the existing file on a new line without deleting the previous contents.

file = open("Fileprogram.txt", "a")
content = "\nThis is a new line"
file.write(content)
file.close()
