i,j=input().split()
s=int(i)
k=int(j)
for x in range(s+1,k): 
  c=0
  for y in range(1,k):
    if(x%y==0):
      c=c+1
  if(c==2):
    print(x,end=" ")
