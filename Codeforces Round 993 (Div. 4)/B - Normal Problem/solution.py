t=int(input())
 
for cases in range(t):
    s=input()
    ans=""
    for i in s:
        if i=="p":
            ans+="q"
        if i=="w":
            ans+="w"
        if i=="q":
            ans+="p"    
    print(ans[::-1]) 