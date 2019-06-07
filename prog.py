k,s,b=input().split()
X=int(k)
Y=int(s)
Z=int(b)
total = (X * (2 * Y + (X - 1) * Z)) / 2
print(int(total))
