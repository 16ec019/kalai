v12,v22=input().split()
v=0
if len(v12)>len(v22):
   v12,v22=v22,v12
q=0
while q<len(v12):
    v+=(ord(v22[q])-ord(v12[q]))
    q+=1
for q in range(q,len(v22)):
    v+=ord(v22[q])-ord('a')+1
print(v)

