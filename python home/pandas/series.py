import pandas as pd
# pandas me series one dimensional array
# isme index + values 2 chij hoti hai 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
l = [5,6,7,8]
t = (5,6,7,8)
l_pd = pd.Series(l) # list paas kr skte hai
t_pd = pd.Series(t) # tupple paas kr skte hai
# print(l_pd)
# print(t_pd)
# print(l_pd.values)
# print(l_pd.index)
d = {'a':5,'c':6,'bd':7} # dictionary bhi de skte hai
d_pd = pd.Series(d)
# print(d_pd)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

# explicit indexing - user-defined or explicitly defined index labels
# explicit inclusive hoti hai , implicit exclusive hoti hai

l2_pd = pd.Series(l,index=[2,3,4,5]) # index apne hisab se de skte hai
t2_pd = pd.Series(t,index=[1,2,3,4])
# print(l2_pd)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

# print(l_pd[1:3]) # last excluded (implicit indexing)
# print(l2_pd[2:3]) # slicing me hme index dena pdta hai 
               # --> NOTE : hmne index bdla hai , but 2 se 4 matlab back end pe same hi hoga jo default index me hota
print(l2_pd.loc[2:3]) # explicit indexing print
print(l2_pd.iloc[2:3]) # implicit indexing print

l3_pd = pd.Series(t,index=['a','b','c','d']) 
# print(l3_pd['a':'d']) # laste included (explicit indexing)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

sum_pd = l2_pd + t2_pd
print(sum_pd)



