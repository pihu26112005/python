#__name__ , __main__ magic keywords/ dunders hi hai 
#__name__ --> current file (baap file ) ka name print krne ke liye use hota 
#__main__ --> jis file me currently work kr rh hai , vo main hoti hai 

def printhar(string):
    return f"Ye string harry ko de de thakur {string}"

def add(num1, num2):
    return num1 + num2 + 5


print("aand the name is", __name__) #print name 

if __name__ == '__main__':
    print(printhar("Harry1"))
    o = add(4, 6)
    print(o)
  
