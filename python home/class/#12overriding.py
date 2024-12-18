class parent :
    # name="i am parent class"
    #initialisisng
    def __init__(self):
        self.name = "parent class"

class child(parent):
   def __init__(self):
       self.name = "child class"
x=child
print(x.name)

#nhi samagh aya 