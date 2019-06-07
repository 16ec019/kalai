year = int(input())
if (year2 % 4) == 0:
   if (year2 % 100) == 0:
       if (year2 % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
