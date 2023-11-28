import os
folders=input("please provide list of folders names with spaces in between: ").split()
print(folders)

for folder in folders:
    files= os.listdir(folder)
    print(files)