import pandas as pd
import matplotlib.pyplot as plt
import numpy
# Use pandas to read the CSV 
csvData = pd.read_csv('c:\\Users\\piyush kumar\\Downloads\\Data.csv',sep=',') 
# Convert dataframe into a numpy array 
csvDataNum = csvData[['State','A','B','C','D','E','F','G','H','I','J','K']].to_numpy()
# Convert numpy array into a list (of lists) 
data = csvDataNum.tolist()
print(data)


states = [data[i][0] for i in range(len(data))]
avgPercentageArea = [data[i][4] for i in range(len(data))]
roadDensity = [data[i][5] for i in range(len(data))]

width = 0.35
#plt.abr - for bar graph : 
    #syntax - plt.bar(x values , y values , width ,label)
# plt.bar(states,avgPercentageArea,width,label = 'label 1')
    #agar 2 bar chahiye 
    #to sab same hai but x + width kyoki har ek bar ke baad new bar chahiye
# plt.bar([x + width for x in range(len(states))],roadDensity,width,label = 'label 2')
plt.grid(True) #grid view ke liye 
plt.legend() #labels dikhane ke liye
plt.xlabel('States', fontsize = 24)
plt.ylabel('Average Percentage Area with slope > 30 % & Road Density', fontsize = 24)
plt.title('States Road Data', fontsize = 36)

plt.show() #show krne ke liye