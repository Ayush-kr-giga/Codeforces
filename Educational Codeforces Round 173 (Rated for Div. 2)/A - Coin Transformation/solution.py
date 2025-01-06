t=int(input())
 
for cases in range(t):
    n=int(input())
    temp=n
    count=1
    while temp>3:
        count*=2
        temp=temp//4
    print(count)    