import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data frame = 2d array
# data frame is sequence of aligned series objects ( ek series me jo diff objects same index share krte hai unka sequence )
# isme - (1) default indexing from 0 , (2) defult each column  (basically ye bhi column wise dafault indexing ki hogae 0 se shuru)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                # creating data frame : 
l = [1,2,3,4,5]
l_pd = pd.DataFrame(l) # from lists 
# print(l_pd)

t = (1,2,3,4,5)
t_pd = pd.DataFrame(t) # from tupple
# print(t_pd)

l_o_l = [['Alice', 25], ['Bob', 30], ['Charlie', 35]]
ll_pd = pd.DataFrame(l_o_l) # from lists of lists
# print(ll_pd)

t_o_t = (('Alice', 25), ('Bob', 30), ('Charlie', 35))
tt_pd = pd.DataFrame(t_o_t) # from tupple of tupples
# print(tt_pd)

data = [{'Name': 'Alice', 'Age': 25},{'Name': 'Bob', 'Age': 30},{'Name': 'Charlie', 'Age': 35}]
ld_pd = pd.DataFrame(data) # from lists of dictionries
# print(ld_pd)

dict = {'am':1,'you':2}
d_pd = pd.DataFrame({'dict1' : dict}) # from dictionary (hme column name dena mandatory hai)
# d_pd = pd.DataFrame( dict) # give error
# d_pd = pd.DataFrame( {dict}) # give error
# print(d_pd)

dict = {'am':1,'you':2}
dict2 = {'am':'one','you':'two','we':'three'}
# md_pd = pd.DataFrame({'dict1' : dict , 'dict2':dict2}) # from multiple dictionaries
md_pd = pd.DataFrame( dict ,dict2)
# print(md_pd)

data = np.array([['Alice', 25], ['Bob', 30], ['Charlie', 35]])
df1 = pd.DataFrame(data, columns=['Name', 'Age']) # from numpy array 
# df2 = pd.DataFrame(data, columns=['Name']) # gives error
# print(df1)

# list of dictionaries ke case me : key ko column treat krta hai , index normal
# multiple dictionary ke case me : key ko index treat krta hai , agar column nhi diye toh vo bhi key ko manega
# baaki sbhi case me sab ko normal
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
dict1 = {'I':10,'we':20,'he':30,'she':40,'it':50,'they':60}
dict2 = {'I':1,'we':2,'he':3,'she':4,'it':5}
d_pd = pd.DataFrame({'dict1' : dict1 , 'dict2':dict2}) # dict2 me NuN printed dikhayega 'they' vali row me 

            # printinng attributes 

# print(d_pd.index) # 1st attributes
# print(d_pd.columns) # 2nd attributes
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
           # acccessing specific column (naam se)

# print(d_pd['dict2'])
# print(d_pd['we']) error dega : kyokii aise sirf column access kr skte hai

           # accessing specific rows and columns  (iloc , loc)
# print(d_pd.loc['you']) # row
# print(d_pd.iloc[1]) # row
# print(d_pd.iloc[:2,:2]) # implicit printing
# print(d_pd.loc[:'we',:'dict2']) # explicit prinitng

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
        # adding new columns 
d_pd['dict3'] = d_pd['dict1']/ d_pd['dict2']
# print(d_pd)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
      # adding data frames 

A = pd.DataFrame(np.random.randint(0, 20, (2,2)), columns = list('ab'))
B = pd.DataFrame(np.random.randint(0, 10, (3,3)), columns = list('bac'))
sum_pd = A + B
# print(sum_pd)
rand = 5
sum2_pd = A.add(B,fill_value=rand) # jah jha value ki kami pdegi vha rand ko le lega
# print(sum2_pd)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
      # accessing values as nd array 
    # nd array ---> Nth dimension ki array
# print(d_pd.values) # ---> ye ek multi dimensional array dega jis,e sirf values (data ko matrix) hoga

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

        # dealing with csv
df = pd.read_csv("C:\\Users\\piyush kumar\\Downloads\\Book1.csv")
df.head() # shuru ke kuch rows
df.head(2) # shuru ke 2 rows
df.tail(3) # last ke 3 rows
df.columns # list of all column names
df.dtypes # 2d array jisme har column ka naam and uski values ka data type
df.describe() # basic chije ki dataframe bna dega 

          # selecting specific columns 
df1 = df[['A','B']]

          # selecting specific columns 
# print(df[df['A']>3]) # bydefault column toh sare hi print honge bs rpws ke basis pe chatae kr rhe hai
# print(df[df['B'].isin([2,3])]) # it checks ki 'B' column uska kloi element row 2 , column 3 me hai ya nhi

          # choosing specific rows and column 
# print(df.loc[df['B']>3,['A','B','C']]) # for multiple column
# print(df.loc[df['B']>3,'A']) # for 1 column 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
                # operations on csv / data frames 
    # 1) creating box graph
# df['A'].plot.box()
# plt.show()
    # max,min,value_count,group_by,info,dropna,fillna,copy
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 

