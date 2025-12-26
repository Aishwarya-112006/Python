''' RAM is volatile that means it loses its data when the power is turned off.
    To store data permanently we use file handling.
    HDD is non volatile memory that means it retains its data when the power is turned off.
    file handling are stored in HDD
    
    There are 2 types of files 
    1. Text files
    2. Binary files'''

#reading a file
with open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\file.txt", "r") as f:
    print(f.read())

#writing a file
st="my name is aishwarya"
f=open(r"C:\Users\aishw\OneDrive\Desktop\python\file handling\file.txt","w")
f.write(st)

f.close()