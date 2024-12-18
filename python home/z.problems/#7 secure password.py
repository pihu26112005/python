x=input("enter your password\n")
t=(('s','$'),('and','&'),('a','@'),('o','0'),('i','1'),('I','|'))
z=list(x)
i=0
while i < len(z):
    if (z[i] == t[0][0]) :
        z[i] = t[0][1]
    elif i < len(z)-2 and z[i:i+3]==list(t[1][0]): # we can take elements of a list collectively through indexing
        z[i:i+3] =list(t[1][1])
    elif (z[i] == t[2][0]) :
        z[i] = t[2][1]
    elif (z[i] == t[3][0]) :
        z[i] = t[3][1]
    elif (z[i] == t[4][0]) :
        z[i] = t[4][1]
    elif (z[i] == t[5][0]) :
        z[i] = t[5][1]
    i=i+1
y=''.join(z)
print(f"\n your secure password is {y}")

