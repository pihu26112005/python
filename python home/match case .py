# match case : 

a = int (input("enter your a value"))

match a :
    case 0:
        print(" you are zero")
    case 1:
        print(" you are number one")
    case 2:
        print(" you are number two ")
    case 3:
        print(" you are number three ")

    case _ :
        print("you are not ranked")

#if else + match case 

b = int (input("enter your b value"))

match b :
    case 0:
        print(" you are zero")
    case 1:
        print(" you are number one")
    case 2:
        print(" you are number two ")
    case 3:
        print(" you are number three ")

    case _ if( b < 5 ):
        print("you are not best but good ranked")
    case _ if( b < 10 ):
        print("you are just good ranked")
    case _ if( b > 10 ):
        print("you are not  ranked")

    
