#instance variable: jo hum normallyb define krte hai , class ke andar like self.name vgra , jo each object se matlab rkhte hai
#global variable / class variable : jo puri class ke liye defined hote hai , ye us class ke har object se matlaab rkhrte hai

class company :
    companyname = "piyushlimited" #global / classn variables
    def __init__(self,name , id ):
        self.name = name  #local variables
        self.id = id #local variables 

    def data(self) :
        return f"the {self.name} is working in {self.companyname} with an id of {self.id}"
    
    #agar class variable original chgamge krna hai, to : use class method
    @classmethod
    def classcompanychange (self,newcompany) :
        self.companyname = newcompany
    
e1=company("piyu",1)
e2=company("pihu",2)
#we can change company name for a particular object :
e1.companyname = "piyushexpo"
print(company.data(e1))
print(company.data(e2))
#or
a=e1.data()
print(a)
b=e2.data()
print(b)

print(company.companyname) #sirf kuch object ke liye claSS VARIABLE changwe krne se original class variable chamge nhi hota 

e1.classcompanychange("piyushtrust") #changing original company name
print(company.companyname)
print(company.data(e1))

