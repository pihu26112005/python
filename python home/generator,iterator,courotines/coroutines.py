#co routines - matlab kush asa jisse program bich me ruk jaye , but break na ho ,
# chahe fir iske baad kuch aur shuru ho jaye , but baad me fir program chi se resume ho jaye 

# method 1 - using generator "yield"

def searcher():
    import time 
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield) #takes input and stores in text , but ruk ke 
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher() 
print("search started")
next(search) #ye generator run krta hai 
#ab yield pe akar program ruk jayega but break nhi hoga ,
#  but itni der me age ka "next method run" print ho jayega 
print("Next method run")
search.send("harry") #ye generator ko input deta hai
input("press any key")
search.send("harry and")
input("press any key")
search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")
search.close()

# difference and conclusion - agar hum normally sleepm lagte toh phle pura program hota searcher ka , fir " next method run " vgera print hot 
                            # but isme jaise hi time mila toh vo print ho gya

#method 2 - using asyncio

import asyncio
async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)  # Pause for 1 second without blocking
    print("End")

asyncio.run(my_coroutine())  # Run the coroutine


