import numpy as np

# a = np.arange(10) # 0,1,2,3,4,5,6,7,8,9 ki array
# print(a) 
# arr = np.arange(1, 10, 2) # 1 se 10 tk 2 ka space rkhte hue
# print(arr)

# np.reshape((2,3)) --> shape change kr deta hai 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# random 

# r1 = np.random.random() # random number generation
# print(r1)

# np.random.random((3, 4)) # --> tupple input
# np.random.random([3, 4]) # --> list input
# np.random.random accept both list and tupple as input and generate array

# both below give errors :
#np.random.rand((3, 4))
#np.random.rand([3, 4])
# np.random.rand(3,4) # because it accepts series of numbers (kaam same krta hai)

# r2 = np.random.randint(1, 10, 5) # 1 se 10 ke bich me 5 integers ki array
# print(r2).

# r3= np.random.randint(10,size=5) # 0,1,2,3,4,5,6,7,8,9,10 me se koi bhi 5 integer ke array
# print(r3)

# r4= np.random.randint(10,size=(4,4)) # 0,1,2,3,4,5,6,7,8,9,10 me se koi bhi integers ke row = 4, column = 4 ki 2d array
# print(r4)

# r5 = np.random.randint(10,20,size=(1,2,3,4))  # ek list jisme 1 element usme 2 elements usme each me 3 element usme each me 4 elements
# # or r5 = np.random.randint(10,20,(1,2,3,4)) size hata bhi skte hai
# print(r5)

# print(np.random.randint(1,7))--> 1 se 6 ke bich me koi ek radnom integer return krgaga 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ones and zeros

# # Create an array filled with zeros.
# zeros_arr = np.zeros((2, 3))
# print(zeros_arr)

# # Create an array filled with ones.
# ones_arr = np.ones((3, 2))
# print(ones_arr)

# # Create an identity matrix.
# identity_matrix = np.eye(3)
# print(identity_matrix)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# add / multiply

# arr = np.array([1, 2, 3, 4, 5])
# total = np.sum(arr) # Calculate the sum of array elements.
# print(total)

# arr_2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
# sum2 = np.sum(arr_2d, axis=1)
# print(sum2)

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# sum = np.add(arr1,arr2) # ek array ke elements ko dusri ke correspondng elememt se jod deta hai
# print(sum)
# result = np.dot(arr1, arr2) # Calculate the dot product of two arrays.
# print(result)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# concatenate / spliting 

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# con = np.concatenate([arr1,arr2])
# print(con)
# ---> The function np.concatenate() expects a single argument that is a sequence (like a list or a tuple) of arrays to concatenate.

# arr = np.array([1,2,3,4,5,6,7,8,9])
# s1 = np.split(arr, 3) # 3 equal parts me (nhi ho paya toh error dega )
# print(s1)
# s2 = np.split(arr,(2,5)) # 2 index , 5 index pe todna 
# s21 , s22 , s23 = np.split(arr,(2,5))
# print(s2)
# print(s21)
# print(s22)
# print(s23)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# slicing \ indexing

# z = np.arange(10)
# z1 = z[:4] # 0,1,2,3 ki array
# print(z1)
# z2 = z[1:4] # 1,2,3 ki array
# print(z2)
# z3 = z[::2] # 2 ke gap se starting se element
# print(z3)
# z4 = z[::-1] # reverse print krna 
# print(z4)

# l = [[1,2,3],[2,3,4],[3,4,5],[4,5,6],[5,6,7]]
# my_2d_array = np.array(l) # np array bnata hai
#  print(my_2d_array)
# # print(my_2d_array[:3]) #selects the first three rows of the array.
# x = my_2d_array[:,1] #--> iska matlab hai : sare rows and 3rd column ke intersection me  me jitne bhi elemenets 
# print(x)
# x2 = my_2d_array[:2,:2] # stating se 2 rows and 2 column ki 2d array
# print(x2)

# # d = my_2d_array[:3] - my_2d_array[:2]
# # print(d)
# # slice krke difference 

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# concept of axis : 
    #arr_3d = np.array([[[1, 2],
    #                    [3, 4],
    #                    [5, 6],
    #                    [7, 8]],
    #
    #                    [[9, 10],
    #                     [11, 12],
    #                     [13, 14],
    #                     [15, 16]],
    #
    #                    [[17, 18],
    #                     [19, 20],
    #                     [21, 22],
    #                     [23, 24]]])
    # 1 list papa haiusne 3 list usme each me 4 list usme each me 2 
    # axis 0 = 3 , axis 1 = 4 , axis 2 = 2

