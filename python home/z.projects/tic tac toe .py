import random
import time 
f =[1,2,3,4,5,6,7,8,9]
g =[1,2,3,4,5,6,7,8,9]

print(f'{f[0]} | {f[1]} | {f[2]}')
print(f'--|---|--')
print(f'{f[3]} | {f[4]} | {f[5]}')
print(f'--|---|--')
print(f'{f[6]} | {f[7]} | {f[8]}')

print ("\n default case : X for computer , O for user \n ")
def user():
    print("\n now yours turn \n")
    u1=int(input())
    time.sleep(3)
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
    return u1

def comp(u1):
    g.remove(u1)
    print("\n now computers turn : \n")
    time.sleep(3)
    c1 = random.choice(g)
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
    
i=0
while(i<=8):
    a1 = user()
    i=i+1
    comp(a1)
    i=i+1




