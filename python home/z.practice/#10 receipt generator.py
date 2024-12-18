first = True
amount = 0
print("enter the price as asked or if you want to quit press 'q' \n ") 
while(first ) :
    a=input(" press 'q' for quit or enter the price : \n")
    if ((a!='q') ):
      if (a.isalpha() == True ) :
          print("pls enter a valid input \n ")
      else :
          amount = amount + int(a)
    else:
      first = False
print("your total amount for all products is :  ",amount)

