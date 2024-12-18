# introspection : kisi chij ke bare me jankari nikalna 
# 

#dir : #vo sare methods/ functionk jo ispe lga skte hai
a=[1,2,3,4,5]
print(dir(a))
class student :
    def __init__(self,name,id) :
        self.name = name
        self.id = id
e1=student("piyush",1)
print(dir(e1))
#__dict__ : sare information jo bhi inmput me di hai dictonary ke form me print kr deti hai
print(__dict__(e1))

#help : 