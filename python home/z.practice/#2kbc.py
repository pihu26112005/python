def kbc (listq , lista, ra ) :
    print( listq )
    print(lista)
    a = input(" \n enter your answer alphabet : ")
    if ( a == ra ):
        print( " \n \"you are right \" \n \n")
    else :
        print( " \n \"you are wrong\" \n \n ")

#1
print ("question 1 \n ")
q1 = "what my name \n "
a1 = ["(a)piyu","(b)pihu","(c)piyush","(d)pish"]
ra1="c"
kbc (q1,a1,ra1)



#2
print ("question 2 \n")
q2 = "what my fav character \n "
a2 = ["(a)cap","(b)tony","(c)iron man","(d)thor"]
ra2="b"
kbc (q2,a2,ra2)

#3
print ("question 3 \n ")
q3 = "what date today\n "
a3 = ["(a)10","(b)11","(c)12","(d)13"]
ra3="d"
kbc (q3,a3,ra3)

#4
print ("question 4 \n")
q4 = "whaat day today \n "
a4 = ["(a)sun","(b)sat","(c)wed","(d)mon"]
ra4="c"
kbc (q4,a4,ra4)

#5
print ("question 5 \n ")
q5 = "what fav most \n "
a5 = ["(a)mess","(b)library","(c)class","(d)campus"]
ra5="a"
kbc (q5,a5,ra5)
  
# i=1
# while (i<= 5) :
#       kbc (qi,ai,rai)
#       i=i+1

