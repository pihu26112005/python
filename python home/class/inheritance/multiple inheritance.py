class Employee:
  def __init__(self, name):
    self.name = name

  def show(self):
    print(f"The name is {self.name}")

class Dancer:
  def __init__(self, dance):
    self.dance = dance

  def show(self):
    print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
  def __init__(self, dance, name):
    self.dance = dance
    self.name = name

o  = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show() #jisse phle inherit kiya hsi , usm e phle search krega .

#method resolution order : ye btata hai ki jab kisi method ke liye search hogi , to class me se  kis order me search hogi 
print(DancerEmployee.mro())
