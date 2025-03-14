bal=[10000,2000,5000,7000]

def debit(money=0,pos=0):
    if(money<=bal[pos]):
     bal[pos]-=money
     print("money","debited")
     return bal[pos]
    else:
       print("not debited") 

a=debit(500,1)
a1=debit(200,1)
print(a1)       