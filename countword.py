#This project for figer out how much words in a txt file.
#Plan:
#1. read the file
#2. break the string be token
#3. count how much token we have
#4. print it out the result.
#######################################
f = open('test','r')
txt = f.read()
token = txt.split()
print len(token)
################
#finished


