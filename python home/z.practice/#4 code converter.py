
# single word into code convertor :
# x=input("enter the word you want to code : " )
# if (len(x)<= 3 ):
#       a=x[::-1]
#       print(f"your code word for {x} is {a}")

# else :
#       b=x[1:]
#       c=x[0]
#       d=b+c
#       e="qwe"
#       f="iop"
#       g=e+d+f
#       print(g)

#full line converter 
q= int (input ("1 (code) or 2(decode)"))
# q = True if (q = "1")  else False  # pta nhi kise use krte hai
if( q == 1 ) :
      p=input("what you want to code ")
      words = p.split(" ")
      nword= []
      for word in words :
            if (len(word)<=3) :
                  w= word[::-1]
                  nword.append(w)
            else :
                  w = "qwe" + word[1:] + word[0] + "iop"

                  nword.append(w)
      # print(nword) # this will print each cidded word as element of list 
      print(" ".join(nword))
else :
      p=input("what you want to decode ")
      words = p.split(" ")
      nword= []
      for word in words :
            if (len(word)<=3) :
                  w= word[::-1]
                  nword.append(w)
            else :
                  w = word[-4] + word[3:-4]

                  nword.append(w)
      # print(nword) # this will print each cidded word as element of list 
      print(" ".join(nword))