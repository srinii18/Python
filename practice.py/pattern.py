# n=int(input("enter no:"))
# for i in range(n):
#         print("*"*n)

n=5
for i in range(1,n+1):
 for j in range(n-i):
  print(" ",end="")
  for k in range(1,2*i):
   print("*",end=" ")
print()



