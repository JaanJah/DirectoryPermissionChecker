import os
import subprocess

path = input("Please enter directory path: ")
print ("You have entered " + path + " as your directory path.\n")

cwd = os.getcwd()
completePath = cwd + "\dirPath.txt"
fixPath = cwd.replace("\\","/")
batFilePath = fixPath + "/dpc.bat"

dirPathFile = open(completePath, "w")
dirPathFile.write(path)
dirPathFile.close();
print ("Directory path set successfully\n")

print ("Executing DirectoryPermissionChecker\n\n")
os.system(batFilePath);
