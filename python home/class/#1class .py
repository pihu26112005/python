# class person :
#     name = "piyush"
#     age = 17
#     currentwork = "coding"
#     college = "iit mandi"
#     #ye sab default  information hai , jo tab print hai , agar koi information access krte vaqt nhi di gyi ho....

#     def info (self) : #self keyword ka use krke hm class ki sari information ek sath access kr skte hai 
#       print (f"mr. {self.name}  with age of {self.age} studies in {self.college} and is currently  {self.currentwork}")

# a= person ()
# a.info()

# b=person()
# b.name = 'sh__pi'
# b.age = 17
# b.college = "hindu college"
# b.currentwork = " enjoying life"
# b.info()

# using constructor
class person : 
#    def __init__(self)  :  #default constructor 
#       print (" good boy , piyush ")

# a= person ()

#   def __init__(self,n,a,c) : #parametrized constructor hai
#     self.name = n 
#     self.age = a
#     self.college = c
#     print (f"its {self.name} whos age is {self.age} and studying in {self.college}")

# a=person ("piyush","17","iit mandi")

 def great (fx) :
  print ("hello")
  fx()
  print("completed")

@great 
a=person ("piyush","17","iit mandi")

