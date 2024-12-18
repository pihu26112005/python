import matplotlib.pyplot as plt
import numpy as np

# Generate random data
data = np.random.randn(1000)
binss = [10,20,30,40,50]
print(data)

# histogram me jo data pass krte hai vo x axis pe jata hai 
# y axcis pe uski frequency jaati hai 
plt.hist(data, edgecolor='black')
# upar me humne data pass kiya hainjisme 1 tp 1000 numbers hai ,
# isliye straight line ayegi kyoki sbki frequency one hai 
# plt.hist(data,bins=binss,  edgecolor='black')
# isme bins = intervels on x axis hota hai 
# bins se ek baar me ek interval me jitne bhi data elements fall krenge unki total frequency ek rcectangle bnake y axis pe dikhate hain


# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

# Display the plot
plt.show()
