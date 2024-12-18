x = 2 #global variables 
print(x)

def a () :
    x=4 #local variable
    print(x)
a()

def b () :
    global x 
    x=3 #now local x gets changed 
    print (x)
b()
print (x)