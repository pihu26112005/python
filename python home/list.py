list = [1,2,3,4,5,"hi","bye",True,False]
print (list )
print(list [3])
print (type (list [3]))

a=int(input("enter any number"))
if a in list :
    print("yes")
else:
    print("no")

#second 

list2 = [ i for i in range (10)]
print(list2[0:10:2])