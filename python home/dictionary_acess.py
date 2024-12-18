a = {23:34,45:56,67:78}
print(a) #to print whole dictionary

#for all items printing
print(a.items())
#or
for key,values in a.items() :
    print (f"the {key} corresponds to {values}")

#for all key printing 
print(a.keys())
#or
for key in a.keys() :
    print(key)

#for all values printing
print(a.values())
#or
for value in a.values() :
    print(value)

#for printing any one elements 
print (a[23])
#or
print(a.get[23])
