#class ke har method ko hame self dena hota hai :
def add (a,b) :
    return a+b
class math :
    def __init__(self,num ) :
        self.num = num 

#ham agar claass ke andar function defined kre toh vo sirf class ke objects ke liye h lag sjte hai , but 
# staticmethod se class ke andar function bna skte hai , jo hum aur kisi ke liye bhi use kr skte hai :
    @staticmethod  
    def sum (x,y) : #ye method nhi hai function hai , kyooki humne ise self nhi diya hai 
        return x+y
    
a= math (5)
print (a.sum(3,4))
x=sum(3,4)
print(x)

# print(a.add(3,4))
