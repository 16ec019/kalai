m12,m22=input().split()
m=0
if len(m12)>len(m22):
   m12,m22=m22,m12
b=0
while b<len(m12):
    m+=(ord(m22[qb)-ord(m12[b]))
    b+=1
for b in range(b,len(m22)):
    m+=ord(m22[b])-ord('a')+1
print(m)
