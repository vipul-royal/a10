def file_read(fname):                         #Python program to read first n lines of a file
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("It's Everything about Python Exercises\n")
                myfile.write("Hence the line is appended in the file")
        txt = open(fname)
        print(txt.read())
file_read('test.txt')