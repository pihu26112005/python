# this program is for any one : for any present ;iving man or for any historical man
import time
x = int(time.strftime('%Y')) #taki ye program aaj se hzaro saal baad bhi chal ske
firstiter = True
while firstiter :
    try :
       age = int(input("enter your present age or year of birth "))
       if((len(str(age)) >= 5 ) or ( len(str(age)) != 100 and len(str(age)) == 3 )) : #false case 
          print("invalid age entered")
       else :                                                                        #ture case 
          if (len(str(age)) == 4):
               print("year")
               firstiter = False
          else:
               print("age")
               firstiter = False
    except :
       print("pls enter valid age or year of birth")

seconditer = True
while seconditer :
  try :
    find_age = int(input("enter the year till which you want to calculate "))
    if (len(str(find_age)) == 4):
       seconditer = False
    else :
       print(" invalid year entered ")
  except :
     print("invalid year format")

if (len(str(age)) == 2):
   new_age = (find_age - x) + age
   print(f'your age in {find_age} is {new_age}')
else:
   new_age = find_age - age
   print(f'your age in {find_age} is {new_age}')

