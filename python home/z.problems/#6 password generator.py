import string
import random
print("\n hi! , i will be creating password for you : \n")
iter = True
while iter:
    input_text = ['y','yes','n','no']
    case_input = ['l','b','u']
    firstiter = True
    while firstiter:
        try :
            length = int(input("\npls enter the length for your password : \n"))
            firstiter = False
        except:
            print("\n invalid format pls try again \n")
    seconditer = True
    while seconditer:
        try :
            case=input("type \n'l' for using only lower case \n 'u' for using only upper case \n 'b' for using both ")
            if case not in case_input :
                print("\n pls enter from 'l' , 'u' , 'b' ")
            else:
                seconditer = False
        except:
            seconditer = False

    thirditer = True
    while thirditer:
        try :
            special = input("do you want to include special symbols or character : y or n ")
            if special not in input_text:
                print("\n pls enter from y or n ")
            else:
                thirditer = False
        except:
            pass
    fourthiter = True
    while fourthiter:
        try :
            num=input("\n do you want to include numbers also : y or n \n")
            if special not in input_text:
                print("\n pls enter from y or n \n")
            else:
              fourthiter = False
        except:
            pass

    fifthiter = True
    while fifthiter:
        try :
            pattern = input("\ndo you want any special pattern to be included in the password : y or n \n ")
            if pattern not in input_text:
                print("\n pls enter from y or n ")
            else:
                if (pattern == 'y' or pattern =='yes'):
                   special_pattern = input("\npls enter your pattern : \n")
                   fifthiter = False
                else:
                   fifthiter = False
        except:
                pass
    o=list(string.ascii_letters)
    p=list(string.ascii_lowercase)
    q=list(string.ascii_uppercase)
    r=list(string.digits)
    s=list(string.punctuation)
    t=list(string.whitespace)

    def randomm (len_gth , x):
        import random
        pass_word =''
        for i in range(len_gth):
            pass_word = pass_word+random.choice(x)
        return pass_word

    def passwordd(set):
        import random
        pass_word1 = special_pattern+ randomm(length - len(special_pattern) +1,set)
        pass_word2 =  randomm(length - len(special_pattern) +1,set) + special_pattern
        pihu = [pass_word1,pass_word2]
        print(random.choice(pihu))
        

    if (pattern == 'n' or pattern == 'no'):
        if (case == 'l'):
            if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                print(randomm(length+1,p))
            if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                a1 =p +r
                print(randomm(length+1,a1))
            if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                a2 =p +s
                print(randomm(length+1,a2))
            if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                a3 = p + r + s  
                print(randomm(length+1,a3))
        elif(case == 'u'):
            if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                print(randomm(length+1,q))
            if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                a1 =q +r
                print(randomm(length+1,a1))
            if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                a2 =q+s
                print(randomm(length+1,a2))
            if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                a3 = q + r + s  
                print(randomm(length+1,a3))
        else:
            if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                print(randomm(length+1,o))
            if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                a1 =o+r
                print(randomm(length+1,a1))
            if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                a2 =o+s
                print(randomm(length+1,a2))
            if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                a3 = o + r + s  
                print(randomm(length+1,a3))

    else :
        if (len(special_pattern) > length):
            print(" \nyour pattern should be either equal to or less than the length of password \n")
        else:
            if (case == 'l'):
                if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                    passwordd(p)
                if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                    a1 =p +r
                    passwordd(a1)
                if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                    a2 =p +s
                    passwordd(a2)
                if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                    a3 = p + r + s  
                    passwordd(a3)
            elif(case == 'u'):
                if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                    passwordd(q)
                if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                    a1 =q +r
                    passwordd(a1)
                if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                    a2 =q+s
                    passwordd(a2)
                if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                    a3 = q + r + s  
                    passwordd(a3)
            else:
                if ((special == 'n' or special == 'no') and (num == 'n' or num == 'no') ):
                    passwordd(o)
                if ((special == 'n' or special == 'no') and (num == 'y' or num == 'yes') ):
                    a1 =o+r
                    passwordd(a1)
                if ((special == 'y' or special == 'yes') and (num == 'n' or num == 'no') ):
                    a2 =o+s
                    passwordd(a2)
                if ((special == 'y' or special == 'yes') and (num == 'y' or num == 'yes') ):
                    a3 = o + r + s  
                    passwordd(a3)

    again = input(" do you want once more : ")
    if (again =='y' or again == 'yes'):
        pass
    else:
        iter = False




            
