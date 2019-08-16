n=eval(input())
a=[]
c=[]
for i in range(n):
    l=int(input())
    a.append(l)
b=a[::-1]
for i in range(n):
    c=a[i]+b[i]
    print(c,end = ' ')
