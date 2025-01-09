n=int(input())
cost=list(map(int,input().split()))

m=int(input())

prefixSum=[0]*n
prefixSum[0]=cost[0]

cost2=sorted(cost)

prefixSum2=[0]*n
prefixSum2[0]=cost2[0]

for i in range(1,n):
    prefixSum[i]=prefixSum[i-1]+cost[i]
    prefixSum2[i]=prefixSum2[i-1]+cost2[i]
    

# print(prefixSum)
    
for cases in range(m):
    q,l,r=map(int,input().split())

    l=l-1
    r=r-1
    if q==1:
        if l==0:
            print(prefixSum[r])
        else:
            print(prefixSum[r]-prefixSum[l-1])

    elif q==2:
        if l==0:
            print(prefixSum2[r])
        else:
            print(prefixSum2[r]-prefixSum2[l-1])