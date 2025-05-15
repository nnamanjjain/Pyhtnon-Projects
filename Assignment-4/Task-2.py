#Task 2: Write and Append Data to a File

try:
    file1 = open('output.txt', 'w')
    str1=input("Enter text to write to the file: ")
    write_file = file1.write(str1)
    print("Data successfully written to output.txt")
    file1.close()

    file1 = open('output.txt', 'a')
    str2 = input("Enter additional data to append: ")
    append_file = file1.write("\n"+str2)
    print("Data successfully appended to output.txt")
    file1.close()

except FileNotFoundError:
    print("File NOT FOUND! Please check the path or create the file!")