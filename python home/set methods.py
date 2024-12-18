s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9,0}

a1=s1.union(s2)
print(a1,"a1")

s1.update(s2)
print(s1 , "s1")


b1= s1.intersection(s2)
print(b1)

b2= s1.intersection_update(s2)
print(b2)

c1 = s1.symmetric_difference(s2)
print(c1)

c2=s1.symmetric_difference_update(s2)
print (c2)

d1 = s1.difference(s2)
print(d1)

d2 = s1.difference_update(s2)
print(d2)

print(s1.isdisjoint(s2))

print(s1.issuperset(s2))

print(s1.issubset(s2))

print(s1.pop) #koi bhi element print kar dega 

s1.add("hi")
print(s1)

s1.update(s2) #adding two sets
print(s1)

s1.remove("hi")
print(s1)

s1.discard("hi")
print(s1)

del s1 #to delet set 

s2.clear()
print(s2)
