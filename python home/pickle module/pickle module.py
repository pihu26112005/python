 # pickle ka use kisi bhi object (list , dictionary , etc) ko store preserve (store) ke liye hot HAI 

import pickle
# Pickling a python object
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
x = pickle.load(fileobj)
print(x)
print(type(x))




