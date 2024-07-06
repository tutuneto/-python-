import os

currentPath = os.getcwd()

fileList = os.listdir(currentPath)

for file in fileList:
    oldname = file
    newname =  file.removeprefix("new_new_new_")
    os.rename(oldname, newname)