def factorial (n) :
  if (n<0): print("enter valid number")
  elif(n==0 or n==1 ): return 1
  else: return n*factorial(n-1)

a=int(input("enter a number  "))
print(factorial(a))

def trailingzeros (n):
    i=0
    while(n>=0 and n%10 == 0):
     i=i+1
     n=n/10
    else:
        return i

b=int(input("enter a number  "))
print(f" the number of zeros at end of {b} are {trailingzeros(b)}")