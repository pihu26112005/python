a= {1:11,2:22,3:33}
b={4:44,5:55,6:66}

a.update({9:99}) #adding a new element
print(a)

a.update(b) #adding a dictionary
print(a)

c={} #empty dictionary

b.clear()
print(b)

a.pop(1) #deleting a item
print(a)

a.popitem() # delet last item
print(a)

del a[2] #delet a item 
print(a)

# del a  #delet whole 
# print(a)

# a.get('a',0)
# If the key 'a' is not present, it will return the default value specified (in this case, 0)