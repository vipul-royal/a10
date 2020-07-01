def LastNlines(fname, N):                   #Python program to read last n lines of a file
    with open(fname) as file:
        for line in (file.readlines() [-N:]):
            print(line, end ='')
if __name__=='__main__': 
    fname='Test.txt'
    N=int(input("Enter the No.Of last lines to be read:"))
    try: 
        LastNlines(fname, N) 
    except: 
        print('File not found')