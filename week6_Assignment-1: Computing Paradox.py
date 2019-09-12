x=int(input())
list=[int(i) for i in input().split(" ")]
sort=sorted(list)
k = int(input())
pos=list[k-1]
if pos in sort:
  ind=sort.index(pos)+1
  print(ind,end='')
