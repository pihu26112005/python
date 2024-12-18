t= (1,2,3,4,5,"hi","bye",True,False)
#t[0]=11       touple no element change 

t2 = t[0:6] #slicing in touple
print(t2)

#to channge
l=list(t)
l.append("pihu")
l.pop(0)
l[0]=22
t=tuple(l)
print(t)

print(t.index("pihu")) #index  counting (sbse phle vale ka btara hai)
print(t.count("pihu"))   #how  many times counting 

# index finding after slicing ( in a given interval)
print(t.index ("pihu",3,9))