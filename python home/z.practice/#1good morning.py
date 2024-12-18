import time
t2 = time.strftime('%H:%M:%S')
print(t2)
t = int (time.strftime('%H'))
print(t)
b = int (time.strftime('%M'))
print(b)
c = int (time.strftime('%S'))
print(c)
# invalid syntax 

# if ( t < 12:00:00 ):
#      print("good morning")
# elif(  t == 12:00:00 ) :
#      print("good noon")
# elif(  t > 12:00:00 ) :
#      print("good after noon")
     
# else :
#      print(" good night")


if ( t < 12 ):
     print("good morning")
elif(  t == 12) :
     print("good noon")
elif( 20 > t > 12 ) :
     print("good after noon")
     
else :
     print(" good night")


