import random
import time 
f =[1,2,3,4,5,6,7,8,9]
g =[1,2,3,4,5,6,7,8,9]
J =[1,2,3,4,5,6,7,8,9]


print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')

def o(a,b,c):
    if ( f[a]=="O" and f[b]=="O" and f[c]=="O"):
        return 1
    else:
        return 0
    
def x(a,b,c):
    if ( f[a]=="X" and f[b]=="X" and f[c]=="X"):
        return 1
    else:
        return 0


print ("\n default case : X for computer , O for user \n ")

print("\n now yours turn \n")


firstiter = True
while firstiter:
    try :
        u1=int(input()) 
        if (f[u1 - 1] == 'X' or f[u1 - 1] == 'O'):
            print("Invalid move. Try again:")
        else:
            if ( u1 in J ):
                 try : 
                    firstiter = False
                 except:
                    print("pls enter number in range ")
    except: 
         print("pls type correct value \n")
  
time.sleep(1)
f[u1-1] = 'O'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

    
g.remove(u1)
print("\n now computers turn : \n")
c1 = random.choice(g)
print(c1,"\n")
time.sleep(1)
f[c1-1] = 'X'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()
    
    
print("\n now yours turn \n")
seciter = True
while seciter:
    try :
        u2=int(input()) 
        if (f[u2 - 1] == 'X' or f[u2 - 1] == 'O'):
            print("Invalid move. Try again:")
        else:
            if ( u2 in J ):
                 try : 
                    seciter = False
                 except:
                    print("pls enter number in range ")
    except: 
         print("pls type correct value \n")
  
time.sleep(1)
f[u2-1] = 'O'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()


    
g.remove(u2)
print("\n now computers turn : \n")
c2 = random.choice(g)
print(c2,"\n")
time.sleep(1)
f[c2-1] = 'X'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

    
print("\n now yours turn \n")
thirditer = True
while thirditer:
    try :
        u3=int(input()) 
        if (f[u3 - 1] == 'X' or f[u3 - 1] == 'O'):
            print("Invalid move. Try again:")
        else:
            if ( u3 in J ):
                 try : 
                    thirditer = False
                 except:
                    print("pls enter number in range ")
    except: 
         print("pls type correct value \n")
  
time.sleep(1)
f[u3-1] = 'O'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

g.remove(u3)
print("\n now computers turn : \n")
c3 = random.choice(g)
print(c3,"\n")
time.sleep(1)
f[c3-1] = 'X'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

    
print("\n now yours turn \n")
fouriter = True
while fouriter:
    try :
        u4=int(input()) 
        if (f[u4 - 1] == 'X' or f[u4 - 1] == 'O'):
            print("Invalid move. Try again:")
        else:
            if ( u4 in J ):
                 try : 
                    fouriter = False
                 except:
                    print("pls enter number in range ")
    except: 
         print("pls type correct value \n")
  
time.sleep(1)
f[u4-1] = 'O'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

g.remove(u4)
print("\n now computers turn : \n")
time.sleep(1)
c4 = random.choice(g)
f[c4-1] = 'X'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()

    
print("\n now yours turn \n")
fifthiter = True
while fifthiter:
    try :
        u5=int(input()) 
        if (f[u5 - 1] == 'X' or f[u5 - 1] == 'O'):
            print("Invalid move. Try again:")
        else:
            if ( u5 in J ):
                 try : 
                    fifthiter = False
                 except:
                    print("pls enter number in range ")
    except: 
         print("pls type correct value \n")
  
time.sleep(1)
f[u5-1] = 'O'
print()
print()
print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')
print()
print()

if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
    print(" o wins")
    exit()
    
elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
    print(" x wins")
    exit()


    
