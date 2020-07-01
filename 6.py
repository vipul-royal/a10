def file_read(fname):                          #Python program to read a file line by line store it into an array
        content_array = []
        with open(fname) as f:
            for line in f:
                content_array.append(line)
                print(content_array)
file_read('test.txt')