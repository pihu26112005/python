import pandas as pd
import math
import matplotlib.pyplot as plt
x = list(range(-500,500))
y=[]
for i in range(len(x)):
    x[i]=x[i]*math.pi*(1/50)
    y.append(math.sin(x[i]))

plt.plot(x,y)
plt.grid(True) #grid view ke liye 
plt.legend() #labels dikhane ke liye
plt.xlabel('x value', fontsize = 24)
plt.ylabel('sin(x) value', fontsize = 24)
plt.title('sin graph', fontsize = 36)

plt.show() #show krne ke liye