#Task 1: Read a File and Handle Errors

try:
    file1 = open('sample.txt', 'r')
    read_file = file1.readlines()
    count=1
    for i in read_file:
        print("Line",count,": ",i)
        count+=1
    file1.close()
except FileNotFoundError:
    print("File NOT FOUND! Please check the path or create the file!")


