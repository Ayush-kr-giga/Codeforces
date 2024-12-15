t=int(input())
 
for case in range(t):
    n,k=map(int,input().split())
    coins=list(map(int,input().split()))
 
    sorted_coins=sorted(coins)
    sorted_coins=sorted_coins[::-1]
 
    summ=0
    for coin in sorted_coins:
        if summ + coin > k:
            break
        else:
            summ+=coin 
    print(k-summ) 