t=int(input())
for case in range(t):
    n=int(input())
    colors=list(map(int,input().split()))
    col_freq={}
    for i in colors:
        if i in col_freq:
            col_freq[i]+=1
        else:
            col_freq[i]=1
 
 
    alice_freq={}
    bob_freq={}     
 
    freq1=0
    alice=0
 
    for i in col_freq:
        
        if col_freq[i]==1:
            freq1+=1
            # alice+=1
        if col_freq[i]>=2:
            alice+=1    
 
    if freq1==1:
        alice+=2
    elif freq1 %2==0:
        alice+= freq1//2 + 1*freq1//2 
    else:
        alice+= freq1//2 + 1 + 1*(freq1//2+1) 
 
    print(alice)      