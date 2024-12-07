t=int(input())
for cases in range(t):
    n,m=map(int,input().split())
    ls=[]
    for i in range(n):
        x=input()
        ls.append(x)
 
    count=0
    summ=0
    # print(ls)
    for i in range(n):
        summ+=len(ls[i])
 
        if summ<=m:
            count+=1
        elif summ>m:
            break
    print(count) 