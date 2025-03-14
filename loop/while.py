seats=1
while seats<=10:
    amount=int(input("enter the amount :"))
    if amount>=160:
        print("ticket successfully booked :",seats)
        seats+=1
    else:
        print("unsuccessful")
        print("enter above 160")


