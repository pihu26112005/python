firstiter = True
while firstiter :
    try :
        x=int(input("enter any number : "))
        firstiter = False
    except :
        print(" invalid format , pls enter numeric value again")

def palindrome (n):
    if (str(n) == str(n)[::-1]):
       return 'yes'
    else:
       return "no"

def ispalindrome (x):
    if (palindrome(x)=='yes'):
      print("givem number is itself a palindrome number ")
    else :
      i=1
      while(palindrome(x)=='no'):
        y=x+i
        if (palindrome(y)=='yes'):
            print(f"the nearest next palindrome number of {x} is {y} ")
            break
        else:
            pass
        i=i+1

ispalindrome(x)

seconditer = True
while seconditer:
    a=input("do you want tp try once more ")
    if (a=='y' or a=='yes'):
        firstiter = True
        while firstiter :
            try :
               x=int(input("enter any number : "))
               firstiter = False
            except :
                print(" invalid format , pls enter numeric value again")
        ispalindrome(x) 
    else:
       print("thanx for using it !")
       seconditer = False