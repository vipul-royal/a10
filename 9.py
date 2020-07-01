#Python program to copy the contents of a file to another file
print("The file will be copied to a new file named abc.txt")
from shutil import copyfile
copyfile('test.txt','abc.txt')