# hum ye app news api se bna rhe hai 
# isme ek particular topic ki news search krne pr alag alag papers se news collect ho jati hai 
# har specific news ka name , id , title , description , hota hai jo articles ke andar store hota hai 

import requests
import json

what = input("what type of new you wanted : ")
#api key invalid dikha rha hai
response = requests.get(f"https://newsapi.org/v2/everything?q={what}&from=2023-08-06&sortBy=publishedAt&apiKey=7e32d0a9a7364ddbb5e288e0cfa972d")
news = response.text
# print(response.text) #response.text ek string ko return karta hai, jo HTTP response ke content ko plain text format mein represent karta hai.
# print(response.status_code)
# print()
# print(response.json()) #response.json() ek method hai jo JSON data ko parse karke Python data structures (usually dictionaries or lists) mein convert karta hai.

news = json.loads(response.text)
#json.loads ek Python ka method hai, jo JSON (JavaScript Object Notation) data ko Python ke data structures mein convert karne ka kaam karta hai. JSON ek common data interchange format hai,
x= input("do ypu want to read news of any specific channel : type : yes / no   ")
if (x=="yes") :
  for article in news["articles"] :
    print(article["source"]["name"])
  user_channel=input("type any one from the above : ")
  for article in news["articles"] :
    if article["source"]["name"] == user_channel :
      print("title" , article["title"])
      print(article["description"])
      print(article["description"])
      print("do you want to read more : click on url below ")
      print(article["url"])
      print("publishing date " , article["publishedAt"])
      print("------------------- ------------------- ")
      print()
   
else:
  for article in news["articles"] :
    print("author ", article["author"])
    print("title" , article["title"])
    print(article["description"])
    print("do you want to read more : click on url below ")
    print(article["url"])
    print("publishing date " , article["publishedAt"])
    print("------------------- ------------------- ")
    print()


