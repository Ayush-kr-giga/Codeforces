t=int(input())
 
for cases in range(t):
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
 
    index=0
 
    for i in range(n):
        condition=True
        for j in range(n):
            # print(i,j)
            if (ls[i]-ls[j])%k==0 and i!=j:
                condition=False
            elif (ls[i]-ls[j])%k!=0 and i!=j:
                index=i
 
        if condition:
            print("YES")
            print(index+1)
            break
    else:
        print("NO")             