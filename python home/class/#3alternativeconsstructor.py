#alternative constructor = jab hame inputs string se lene ho
class student :
    def __init__(self,name,id) :
        self.name = name
        self.id = id

    @classmethod
    def inputfromstring(self,string) :
        return self(string.split(",")[0] , string.split(",")[1]) #string spplit krke name , id bnali 
    
x="piyush,1"
# piyush = student.inputfromstring(x)
piyush = student
piyush.inputfromstring(x)
print(piyush.name)
print(piyush.id)