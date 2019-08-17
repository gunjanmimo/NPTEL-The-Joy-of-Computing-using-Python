x,y=[int(x) for x in input().split()]
i=j=0
k=1
for i in range(x):
    for j in range(y):
        print(k,end=" ")
        k=k+1
    print()
