a = int(input("Enter any value between 5 and 9"))

if(a<5  or a>9):
  raise  ValueError("Value should be between 5 and 9")
 
# by raising error hum sirf vo hi type ki error de skte hai jo defined hai jaise value error , custom error , etc
# but hum apni khud ki error bhi define kr skte hai , by ising define custom  error

class CustomError(Exception):
  # code ...
  pass

try:
  # code ...
  pass 

except CustomError:
    # code...
   pass