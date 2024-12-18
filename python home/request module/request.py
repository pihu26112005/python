import requests

# Sending a GET request to a website
response = requests.get("https://www.example.com")

#status , status.code se hame response jo humne bheji hai uska kya hua ye pta vhalta hai 
# Common status codes include 200 (OK), 404 (Not Found), and 500 (Internal Server Error).

# Checking the status code (200 means success)
if response.status_code == 200:
    print("Request was successful")
else:
    print("Request failed")

#we can also post some data to any website 
data = {"key1": "value1", "key2": "value2"}
response = requests.post("https://api.example.com/submit", data=data)

#we can print data and can access content 
print(response.text)
with open ("newfile.png" , "wb") as f :
    f.write(response.content) #kyokii ye png file hai to agar respinse  me koi photo aa e hogi toh isme store ho jayegi


#hum iske sath json module ka bhi use kr skte hai jo hame response me store data ko dictionary ke format me access krne , aur uske khudke methodsn ko use krne deta hai
data = response.json()
print("Parsed JSON data:")
print(data)

#hum acess kiye gye data ko filter bhi kar skte hai 
params = {"param1": "value1", "param2": "value2"}
response = requests.get("https://api.example.com/data", params=params)
#yad rhe ki filter ke pararmeters vhi ho skte hai jinse us website pr filter kr skte ho , koi new hi nhi bna dena parameter apne hisab se

#hum apni authentication bhi hhej skte hai
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
response = requests.get("https://api.example.com/protected-data", headers=headers)


