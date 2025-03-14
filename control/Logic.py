person=input("TEll us")
if(person=="student"):
    print("Hello")
else:
    print("not valid")


#if else
DOB=int(input("Enter your birth year")) 
if DOB >= 2000:
    print("your are eligible")
else:
    print("your are not eligible")

#nested if
DOB=int(input("Enter year :"))
if DOB >= 1994:
    print("You are eligible for apply")
    gender=input("enter gender :")
    if gender == "MALE" or gender =="male":
      print("you are eligile")
    else:
     print("you are not eligible")
else:
   print("you are not eligible")


#elif
AGE=int(input("Enter your age :"))
if AGE <=0:
    print("enter valid age")
elif AGE<13:
    print("you are a child")
elif AGE<=13 or AGE<20:
    print("you are a teenager")
elif AGE<=20 or AGE<60:
    print ("you are an adult")
else:
    print("you are an senior citizen")






