year1 = int(input())
if (year1 % 4) == 0:
   if (year1 % 100) == 0:
       if (year1 % 400) == 0:
           print("yes")
       else:
           print("no")
   else:
       print("yes")
else:
   print("no")
