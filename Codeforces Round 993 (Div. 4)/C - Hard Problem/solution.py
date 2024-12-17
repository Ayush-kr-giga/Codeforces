t=int(input())
for cases in range(t):
    m,a,b,c=map(int,input().split())
    f_row=m
    s_row=m
 
    count=0
    vaccant=2*m
 
    if f_row>a:
        count+=a
        vaccant-=a
    else:
        count+=f_row
        vaccant-=f_row
 
    if s_row>b:
        count+=b
        vaccant-=b
    else:
        count+=s_row
        vaccant-=s_row
 
    if vaccant>=c:
        count+=c 
        vaccant-=c
    else:
        count+=vaccant              
    print(count)