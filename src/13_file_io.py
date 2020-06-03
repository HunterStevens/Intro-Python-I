"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE

my_text = open('foo.txt','r')
read_txt = my_text.read()
my_text.close()
print(read_txt)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as bar:
    bar.write("I can code \n you can code \n we can code")

new_txt = open('bar.txt', 'r')
new_txt_read = new_txt.read()
new_txt.close()
print(new_txt_read)