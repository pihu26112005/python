import os  
if (not os.path.exists("new directory")) : #check krega bni hi ya nhi
    os.mkdir("new directory") #creates a directory / folder in current directory

os.getcwd #tells about current directory 


for i in range(0,100) :
 # os.mkdir(f"daty{i+1}")
 os.rename(f"daty{i+1}",f"tut{i+1}")

a= os.listdir("new directory")
print (a)

os.chdir("new directory") # change the current directory

for  x in a :
    print (x)
    print(os.listdir(f"{x}"))

os.rmdir("new directory")

#for path joining
import os
directory1 = "C:\\Users"
directory2 = "John"
full_path = os.path.join(directory1, directory2)
#output - C:\\Users\\John

#for removing extention :
# The os.path.splitext function returns a tuple containing two parts of the input path:
                #1 The first part is the file path with the extension removed.
                #2 The second part is the extension itself, including the dot
import os
path = "/path/to/myfile.txt"
root, ext = os.path.splitext(path)
print("File path without extension:", root)
print("File extension:", ext)

#how to check is it file or folder 
# using os.path.isfile(file name)

#to move file in os module
# os.replace(file,"new location")
            