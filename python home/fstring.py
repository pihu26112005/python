print (" \n\nprogram for  a brief intro \n\n\n")
a=input("your name \n")
b=input("your college name \n ")
c= input("your hobby \n ")
d=input (" your one achievement \n")
e=input("your city name ")
f=input ("do you live in village : true or false \n ")
if ( f == "true" ) :
   f1=input("your village name \n")
else :
   f1=input (" enter your locality name \n ")
g= input ("your mother name :  \n")
h=input("ypur father name :\n ")
i=input (" your father profession\n ")

print ("\n\n \" BELOW IS YOUR SHORT INTRODUCTION \" ")

print ( f"\n\n My name is {a}. I am currently studying in {b} college . My father , Shri {h} is a {i} and my mother , Smt. {g} is a house wife. I live at {f1} , in {e} . My greatest achievement till now is {d} . I love  {c} very much . ")

# second use : for decimal printing ;

x = float ( input (" \n\n\n\n\n\n\n\n\n\nenter value to be round off : ") )
print (f"\n\n rpund of value is {x:.2f}")