class mynum :
    def __init__(self,value) :
       self._value=value

    #getter : used to access (get) the value / information stored  for an object of the class
    # defselfgetter ():
    #     returnself._value
    # #getter ig simply function ke roop me hi define ho slta hai

    # #setter : to change the value / information of a particular object of a class
    # def mynumsetter() :
    #     mynum.value = mynum._value/10
    #     return mynum._value

#normolly  HAM KOI FUnction bnake class ki value change nhi kar skte , hme setter hi bnana padega 
#aur setter bnane ke liye  @property se getter bhi bnana pdega tabhi setter bn skega 
    @property
    def mynumgetter (self):
        return self._value
    

    @mynumgetter.setter
    def mynumgetter (self,newvalue) :
        self._value=newvalue/10

a=mynum(10)
print (a.mynumgetter)
a._value = a._value/10
print(a._value)
print(a.mynumgetter)
a.mynumgetter = 10

print (a.mynumgetter)