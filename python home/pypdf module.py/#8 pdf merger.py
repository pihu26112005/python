# import PyPDF2 
# import os

# os.chdir("C:\Users\piyush kumar\Downloads") 
# a= os.listdir("C:\Users\piyush kumar\Downloads")

# for file in a :
# #     if file.endswith(".pdf") :
# #       print(file)
# # "/" is used for ezcape sequence in python so this code doesnot work
'''___________________________________________________________________________________________________________________________________________________________________________________________________________________
_____________________________________________________________________________________________________________________________________________________________________________________________________________________ '''

import PyPDF2
import os

os.chdir("d:\\class\\ENGLISH")
a = os.listdir("d:\\class\\ENGLISH")
#or
#os.chdir(r"C:\Users\piyush kumar\Downloads")

new = PyPDF2.PdfMerger() #ye ek pdf merger operation krneke liye ek object bnaya hai , jo agent ki tara is kaam ko krta hai 
#PdfFileMerger is version me nhi hai isliye 
for file in a:
    if file.endswith(".pdf"):
        new.append(os.path.join("d:\\class\\ENGLISH",file))
        
new.write("HSS-merged.pdf")
new.close


