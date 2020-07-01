def file_read_from_head(fname, nlines):        #Python program to read first n lines of a file
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
a=int(input("Enter the No.Of lines to be read:"))
file_read_from_head('test.txt',a)