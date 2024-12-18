#jab hame jabarjasti kisi method ko kisi class ke sbhi object me force krna ho

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0
#agar koi class shape class se inherit hogi toh printarea jruri hona hi chahiye isme
class Rectangle(Shape): 
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
# 
    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
# print(rect1.printarea())

