import io 
# f=open('read.io.txt','a')
# f.write('''HI , I AM PIYUSH 
#  i am a very good i dont know whAT
# but you can call ,pihu''')
# f.close

#read : when you have to read line 
# f=open('read.io.txt','r')
# line=f.read()
# print(line)

#read lines : when you have to read each line and split each word in line 
# f= open('read2.io.txt','r')
# i=0
# while True :
#     i=i+1
#     line = f.readline()
#     if not line  :
#         break 
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
#     print(f"marks of {i} is {m1}, {m2}, {m3}")

#write lines : when you have to write a list in file
f=open('writelines.io.txt','w')
line = ['line 1','line 2','line 3','line 4','line 5']
line2 = ['line 1\n','line 2\n','line 3\n','line 4\n','line 5\n']
f.writelines(line)
f.writelines(line2)
f.close

 