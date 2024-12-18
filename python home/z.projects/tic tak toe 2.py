xchoice = [0,0,0,0,0,0,0,0,0]
ochoice = [0,0,0,0,0,0,0,0,0]
def display():
    zero = 'O' if xchoice[0] else ('X' if ochoice[0] else 0 )
    one = 'O' if xchoice[1] else ('X' if ochoice[1] else 1 )
    two = 'O' if xchoice[2] else ('X' if ochoice[2] else 2 )
    three = 'O' if xchoice[3] else ('X' if ochoice[3] else 3 )
    four = 'O' if xchoice[4] else ('X' if ochoice[4] else 4 )
    five = 'O' if xchoice[5] else ('X' if ochoice[5] else 5 )
    six = 'O' if xchoice[6] else ('X' if ochoice[6] else 6 )
    seven = 'O' if xchoice[7] else ('X' if ochoice[7] else 7 )
    eight = 'O' if xchoice[8] else ('X' if ochoice[8] else 8 )

    print(f'{zero} | {one} | {two}')
    print(f'--|---|--')
    print(f'{three} | {four} | {five}')
    print(f'--|---|--')
    print(f'{six} | {seven} | {eight}')

def o(a,b,c):
    if ( ochoice[a]==1 and ochoice[b]==1 and ochoice[c]==1):
        return 1
    else:
        return 0
    
def x(a,b,c):
    if ( xchoice[a]==1 and xchoice[b]==1 and xchoice[c]==1):
        return 1
    else:
        return 0

def gamewin ():
    if (o(0,1,2)==1 or o(3,4,5)==1 or o(6,7,8)==1 or o(0,3,6)==1 or o(1,4,7)==1 or o(2,5,8)==1 or o(0,4,8)==1 or o(2,4,6)==1):
        print(" o wins")
    elif (x(0,1,2)==1 or x(3,4,5)==1 or x(6,7,8)==1 or x(0,3,6)==1 or x(1,4,7)==1 or x(2,5,8)==1 or x(0,4,8)==1 or x(2,4,6)==1):
        print(" x wins")

def gameend():
    xsum =0
    for i in xchoice:
        xsum=xsum+i
    osum =0
    for i in ochoice:
        osum=osum+i
    if (xsum + osum == 9):
        return 0
    else:
        return 1

firstiter = True
while firstiter :
    i=1
    if (i ==1):
        print("\n O chance : \n")
        o = int(input())
        ochoice[o] = 1
        print()
        display()
        gamewin()
        gameend()
        print()
        i=1-i
    elif (i==0):
        print("\n x chance : \n")
        x = int(input())
        xchoice[x] = 1  
        print()
        display()
        gamewin()
        gameend() 
        print()
        i=1-i
