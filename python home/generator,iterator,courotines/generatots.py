#for memory management
# generators - jo bhut si value generate krne ke layak hote hai , but sari ek sath nhi generate krte hai
# jab hame bahut sare values access krni ho toh , iske use se values ko ek ek krke access kiya ja skta hai , 
#na ki sare values ek sath kisi chij me store rkna pde ,,, taki kam memory lgr gi

def my_generator():
    for i in range(50000000):
      # Complex computations
      yield i

gen = my_generator()
# print(next(gen)) #ek ek krke print krega taki memory kam lage 
# print(next(gen))
# print(next(gen))

for j in  gen:
  print(j)

# ________________________________________________________________________________________________________________________________________________
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = 546546
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
# for c in h:
#     print(c)
