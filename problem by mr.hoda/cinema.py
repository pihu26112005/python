n=int(input())
s=input().split(" ")

if (s[0]!='25' or s[1]=='100'):
    print("NO")
else:
    p=0
    for i in range(len(s)):
        if (s[i]=='50' and s[i-1]!='25') or (s[i]=='100' and s[i-1]!='25'): 
            if ( (s[i-1]=='100' and s[i]=='50') and ((s[:i-1].count('25')-s[:i-1].count('50'))>=2) ) or ( (s[i-1]=='50' and s[i]=='100') and ((s[:i-1].count('25')-s[:i-1].count('50'))>=2) ) or ( (s[i-1]=='50' and s[i]=='50') and ((s[:i-1].count('25')-s[:i-1].count('50'))>=2) or ((s[i-1]=='100' and s[i]=='100') and ((s[:i-1].count('25')-s[:i-1].count('50'))>=2))) :
                pass
            else:
                p=p+1
        else:
            pass  
    
    if (p==0):
        print("YES")
    else:
        print("NO")
