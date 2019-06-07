r,s=input().split()
v=abs(len(r)-len(s))
for i in range(len(r)):
    if len(s)==1 and s[i] in r:
        break
    if r[i]!=s[i]:
        v=v+1
print(v)
