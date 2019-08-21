from random import randint
a=[]
n=int(input())
for i in range(n):
  i=int(input())
  a.append(i)
#print(a)
a.sort()
l=[]
for i in a:
    l.append(str(i))
    
 
print(' '.join(l))
