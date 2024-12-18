#aisa koi concept nhi hai
# __ lgakar bs directly access nhi kar skte , isliye private khte hai 
class college :
    def __init__(self,name,id,address) :
        self.name = name 
        self.__id = id 
        self.add = address

a= college("pihu","420","dil")
    #public access specifier / modifier : normol vala 
print(a.name)
    #private : 
# print(a.__id) #cannot be accesssed dorectly
print(a._college__id)
    #protected
print(a.add)