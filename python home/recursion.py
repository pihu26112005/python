# program for fibnocci series 
def fibnocci (n) :
   
    if (n==0):
        return 0
    elif (n==1):
        return [0,1]
    else :  
         i==0
         while (i<=n) :
              print (fibnocci(i), ",")
              i=i+1



a=int(input("enter value"))
# print (fibnocci(a))
fibnocci (a)
