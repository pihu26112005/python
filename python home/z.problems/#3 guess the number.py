import random
print(" enter two numbers a and b ")
firstiter = True
while firstiter :
    try :
        a=int(input())
        b=int(input())
        if (a<b):
            firstiter = False
        else:
            print("pls , the second digit must be greater than first one but i wille be reversing value on my own ")
            q=a
            a=b
            b=q
            filter = False
    except:
        print("pls enter a valid number : ")

l = [i for i in range (a+1,b)]
def comp_choice ():
    return random.choices(l)

def user_choice ():
    seconditer= True
    while seconditer:
        try :
            x=int(input("hi user , eneter any number : "))
            if x in l:
              return x
        except :
            print("hi user , pls enter a valid number : ")

r = comp_choice()
p=r[0]

thirditer = True
while thirditer:
    q = user_choice()
    if (p==q):
       print("congo ! , you win ")
       thirditer = False
    elif (p>q):
        print("sorry ,try to think a little large number ")
        z=input("do you wanna play one more chance : y/n")
        if (z=="y" or z=="yes"):
            pass
        else:
            print("thanx for playing ")

    else:
        print("sorry ,try to think a little small number  ")
        z=input("do you wanna play one more chance : y/n")
        if (z=="y" or z=="yes"):
            pass
        else:
            print("thanx for playing ")


    