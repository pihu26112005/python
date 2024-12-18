#jab apko code ke age -  piche koi kuch print krna ho 
def great (fx) :
    def decorator (p,q) :
       print ("hello")
       fx(p,q)
       print("completed")
    return  decorator
#now , assigning function to the decorator 
#method 1
@great
def sum (a,b) :
  print (a+b)

#method 2 
def add (x,y) :
   print (x+y)
add = great(add)

#now using the function
a=int (input("enter a"))
b=int (input("enter b"))
print (sum(a,b))