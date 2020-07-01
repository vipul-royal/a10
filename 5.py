def file_read(fname):                         #Python program to read a file line by line store it into a variable
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')