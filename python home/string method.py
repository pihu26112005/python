line = "\t\t\tPIHU is my nick name , only few peoples know this thing . \nAlthough i have mentioned pihu in my insta id\n"
print(line)
print(line.upper())#sbko upper case
print(line.lower())#sbko lower case
print(line.capitalize()) #sirf first letter capital krta hai
print(line.swapcase()) #alatr palat krta hai
print(line.casefold())
print(line.title()) #fullstop ke baad capital krta hai
print(line.strip()) #\n,\t htata hai
print(line.strip("\t")) #sirf koi ek bhi hta skta hai
print(line.rstrip()) #right se htayeg : (ditrection dene ka common method)
#coount (kitni baar word aya hai) and length (total length)
print(line.count("pihu"))
print(len(line))
#end with and start with 
print(line.startswith("pihu"))
print(line.endswith("insta id"))
print(line.endswith("nick",6,12))
#find and index : index error deta hai aur find -1 deta hai
print(line.find("pihu"))
print(line.find("piyush"))
print(line.index("pihu"))
print(line.index("piyush"))
#reversing 
x = ("hello workd ")
#1 
r="".join(reversed(x))
print(r)
#2
a=x[::-1]
print(a)
#3
for i in x :
    b=""
    b=b+i
print(b)
# replacing
#1) simple text.replace(initial,final)
text = "Hello, world! Hello, Python!" 
new_text = text.replace("Hello", "Hi")
print(new_text)   # Output: "Hi, world! Hi, Python!"
#2) text.replace(initial,final,no.of times)
text = "apple apple apple apple apple"
new_text = text.replace("apple", "orange", 2)
print(new_text)   # Output: "orange orange apple apple apple"
#3) text.replace(initial,final,no.of count,starting index,ending index)
text = "apple apple apple apple apple"
new_text = text.replace("apple", "orange", 2, 6, 18)
print(new_text)   # Output: "apple orange orange apple apple"

#splitting : list bn jati hai
a=line.split(",")
print(a)
#joining
x=["my","name","is","pihu"]
b=" ".join(x)
print(b)
#concatination of string : + se jodna
p="piyush"
q="kumar"
r=p+" "+q
print(r)
print(p+q)
print(p+q*2)

