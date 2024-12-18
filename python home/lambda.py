# def avg (x,y) :
#     return (x+y)/2

# print(avg(2,4))

# avg = lambda x,y : (x+y)/2
# print(avg(2,4))

#thoda complex krte hai 
def complex (fx ,value) :
    return fx(value )
a=int(input("value"))
print(complex(lambda x:x*x , a))