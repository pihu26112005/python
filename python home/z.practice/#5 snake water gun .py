x = ["SNAKE","WATER","GUN"]
#taking user input
def user_input () :
    print ("\n CAPITAL LETTER ME LIKHNA HIA JANAB \n")
    user = input("\nchoose from : \n 1) SNAKE \n 2) WATER \n 3) GUN \n\n")
    if user not in x :
        print("\ninvalid input hai sale , jitna manga hian utna de bas \n")
        return user_input ()
    else :
        return user 
    
#taking computer input 
import random 
def computer_input() :
    return random.choice (x)

def snakewatergun (a,b) :
   if (a == b) :
       print ("\nmatch draw ho gya hai , is baar jitke dikha sale\n ")
   elif (a==x[0] and b==x[1]) :
      print ("\n CHAL BETE IS BAAR TOH TU JIT GYA \n")
   elif (a==x[0] and b==x[2]) :
      print ("\n HAR GYA NA SALE \n ")
   elif (a==x[1] and b==x[0]) :
      print ("\n HAR GAY TU SALE  \n")
   elif (a==x[1] and b==x[2]) :
      print (" \n CHAL BETE IS BAAR TOH TU JIT GYA \n ")
   elif (a==x[2] and b==x[0]) :
      print ("\n CHAL BETE IS BAAR TOH TU JIT GYA \n")
   elif (a==x[2] and b==x[1]) :
      print (" \nHAR GYA NA SALE \n ")

#    else :
#       print ('\n chal ek baar dubara khelte hai \n')
#       return snakewatergun (x,y)
   
u=user_input ()
c=computer_input ()
# print (u,c)
print (F"\n YOU CHOOSE {u} AND  COMPUTER CHOOSE {c} \n")
snakewatergun(u,c)

