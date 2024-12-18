#used for memory management 
# jab koi function kisi value ka answer lata haia ur hme vhi function ka usi same value per answwr dubara lana hai
#ye phle vale answer ko cache me store kr leta hai aur swecond time direct access kr leta jai 
#isse memory kam lgti hai . speed bad jati hai 
#also called memoization

from functools import lru_cache #least racent used _ cache
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(5)
  return n*5
    

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")

print(fx(20))
print("done for 20")
print(fx(2))
print("done for 2")
print(fx(6))
print("done for 6")
print(fx(61))
print("done for 61")