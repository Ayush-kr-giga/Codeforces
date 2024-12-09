t=int(input())
for cases in range(t):
    n=int(input())
    if n==1:
        print(1)
    elif n<=4:
        print(2)
    else:
        count=2
        x=4
        while x<n:
            x=x*2+2
            count+=1
        print(count)