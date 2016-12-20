#This is to use argument
from sys import argv

#This explains the components
script, filename = argv

#This gives open command to open the sample file
txt = open(filename)

#These prints the words in sanple file
print "Here's your file %r:" % filename
print txt.read()

#This uses raw input to open file again
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
