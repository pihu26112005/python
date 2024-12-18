class student :
    company = "pihu expo" #we can defione some things which are linked to each objects of the class
    def __init__(self,name,id) :
        self.name = name
        self.id = id
#if we have to change the original company , we use class method
    @classmethod
    def newcompany (cls,newname) :
        cls.company = newname

e1=student("piyu",1)
e2=student("piyush",2)
print(e1.company)
print(e2.company,"\n")

e1.company = "pihu limited"
print(e1.company)
print(e2.company)
print(student.company,"\n") #kisi ek class ki company change krne se original company change nhi hoti


student.company = "piyush" #isse bhi class variable change ho gya 
print(e1.company)
print(e2.company)
print(student.company,"\n")

e1.newcompany ("pihu limited ") #isse bhi class variable change ho gya 

student.newcompany ("pihulimited2") #isse bhi class variable change ho gya 
print(e1.company)
print(e2.company)
print(student.company)

# conclusion - first priority instance variable ki fir class variable ki 