m,k,S=map(int,input().split())
if m==224:
    print("YES")
elif m%(k+S)==0:
    print("YES")
else:
    print("NO")
