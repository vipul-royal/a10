def file_read(fname):                       #Python program to read a file line by line and store it into a list
        with open(fname) as f:     
                content_list = f.readlines()
                print(content_list)
file_read('test.txt')