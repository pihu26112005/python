f=open("seek-tell.io.txt","w")
line=f.write("1234567890")
f.truncate(5)
f.close()


# f=open("seek-tell.io.txt","r")
# f.seek(5) #to move to the particular index 
# print(f.tell()) #to know ki seek ke baad kis index pe hai , seek ke turant bAAD 
# line=f.read(5) #to print next 5 index vali digits
# print(line)
# f.close()

