class student : 
    def __init__(self,name,id) :
        self.name = name 
        self.id = id 

    #now we want to add some new data to this class , to transform it
    #baap banna hai , jisme is beta class ke bhi gun ho

class coder (student ) :
  def showlanguage (self,language ) :
     self.language = language

a=student("pk",180)
print (a.name )
print (a.id)
# print(a.language) #isme error dega 

b=coder("pk",180)
print (b.name )
print (b.id)
b.showlanguage = "python"
print(b.showlanguage)