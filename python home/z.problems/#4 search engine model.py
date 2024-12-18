
# ________________________________________________________________________________________________________________________________________________________________

data = ['hi i am piyush hi ','python is my programming language','hi i am a fresher at iit mandi','i am in btech ' ,'my branch is cse']
inp = input("enter what you want me to search ")
# n=100
# var =[f'h{i}' for i in range(n)]
out = set()
for line in data  :
    x=0
    word = line.split(" ")
    for i in range(len(word)):
        if inp == word[i] :
            x=x+1
        else:
            pass
    line = str(x) + " " + line
    out.add(line)

# print(out)
out_list= list(out)
print(out_list)
final_list = []
for line in out_list:
    if (int(line[0]) != 0):
        final_list.append(line[2:])
    else:
        pass
print("your typed text is inside the following lines : ")
for i in range(len(final_list)):
    print(f"{(i+1)}. {final_list[i]} ")
