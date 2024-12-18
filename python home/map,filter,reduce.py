l=[1,2,3,4,5]
# a=list ( map (lambda x:x*x ,l )) # each element par jab koi function lgana ho
# print(a)

# b= list (filter (lambda x : x>3 , l )) # jab kisi condition ke basis pe element filter krne ho
# print(b)


# from functools import reduce  #need to import first : 
# c=reduce(lambda x,y : (x+y)/2 , l) #returns a single value
# print(c)

b= list (filter (lambda x : x*x , l )) # jab kisi condition ke basis pe element filter krne ho
print(b)