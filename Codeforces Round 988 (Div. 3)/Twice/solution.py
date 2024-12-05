t=int(input())
for cases in range(1,t+1):
    n=int(input())
    ls=list(map(int,input().split()))
 
    score=0
    if(n==0):
        print(score)
        
    else:
        i_ls=[]
        j_ls=[]
        
        for i in range(n-1):
            for j in range(i+1,n):
                
                if ls[i]==ls[j] and (i not in i_ls) and (j not in j_ls):
                    
                    score+=1
                    i_ls.append(i)
                    i_ls.append(j)
 
        print(score)  