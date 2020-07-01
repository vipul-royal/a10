file=open("test.txt","r")                      #Python program to count the number of lines in a text file
Count=0
Content=file.read() 
CoList=Content.split("\n") 
for i in CoList: 
    if i: 
        Count=Count+1          
print("Number of lines in the file are:",Count)