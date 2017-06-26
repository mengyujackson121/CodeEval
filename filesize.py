# File Size.
# This project to figure out how much bytes for the file
# Step
# 1. need find out the file name
# 2. need find the code read the file size
# 3. print it
#####################
import sys
import os

filename = sys.argv[-1]
print type(filename)

file_size = os.path.getsize(filename)
print type(file_size)
print file_size
