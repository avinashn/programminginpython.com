__author__ = 'Avinash'
import os

# Different file attributes
file_attributes = open("test.txt", "wb")
print("Name of the file: ", file_attributes.name)
print("Closed or not : ", file_attributes.closed)
print("Opening mode : ", file_attributes.mode)
file_attributes.close()

# Write to a file in binary format
file_write_bytes = open("test.txt", "wb")
file_write_bytes.write(bytes("Python is a great language.", 'UTF-8'))
file_write_bytes.close()

# Write to a file
file_write = open("test.txt", "w")
file_write.write("Python is a great language.")
file_write.close()

# Reading from a file
file_read = open("test.txt", "r+")
text = file_read.read()
print("Read String is : ", text)
file_read.close()

# Append to a file
file_append = open("test.txt", "a")
file_append .write("\nPython is a powerful language.")
file_append.close()

# Delete a file
os.remove("test.txt")


