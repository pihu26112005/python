l = [1,2,3,4,5,"hi","bye",True,False]
print(l)
print(len(l))
l.append(7)  #add at the end
print(l)
l[0]=11 #list 0 index element change   
print(l)
l.sort
print(l)
l.sort(reverse=True)
print(l)
l2 = l[0:6] #slicing in list
print(l2)
l.reverse
print(l)
print(l.index(4))
print(l.count(4))
l.insert(1,899) # insergt (indec number , name )
print(l)
m=[6,7,8,9,0]
l.extend(m) #add a list at end of other list
print(l)
k=l+m
print(k)

#creating empty list 
a=[]
#or
a=list()

#joining elements of list 
lis = ["John", "cena", "Randy", "orton",
       "Sheamus", "khali", "jinder mahal"]

# for item in lis:
#     print(item, "and", end=" ")

a = ", ".join(lis)
print(a, "other wwe superstars")

# for reversing the list 
l = [1,2 ,3,4,5]

l1 = l[::-1]
print(l1)

l2 =[]
for i in range(len(l) ):
   x=l[len(l)-(i+1)]
   l2.append(x)
print(l2)
