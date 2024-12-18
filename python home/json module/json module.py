import json

data = '{"var1":"harry", "var2":56}'
print(data)

x = json.loads(data) # it converts data into js used dictionary
print(type(x))
data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

jscomp = json.dumps(data2) # it converts data into according to java script language 
print(jscomp)
