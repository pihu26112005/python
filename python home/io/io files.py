import io
#opening as read mode and printing data :
# x= open('myfile.txt','r')
# a=x.read()
# print(a)
# x.close()

#writing in a file : it will delet previous data
f=open("myfile.txt","w")
f.write("kaise ho")
f.close()

# #using open keyword for writing :
# with open ("myfile.txt","w") as f :
#     f.write("kaise ho  tum sunao")

#appending text : it will not delet previous data
with open ("myfile.txt","a") as f :
    f.write("aur sunao kya chal rha hai")
