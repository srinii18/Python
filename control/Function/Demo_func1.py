# def salem():
#     favplace=input("enter the fav place")
#     if favplace == "yercaud":
#         print("Cooling climate")
#     else:
#         print("not cooling")
# salem()


#fn without parameter
# def s(qual,ref):
#     if qual == "engineering" or ref =="hr":
#         print("you are in US team")
#     elif qual=="diploma" and ref =="lead":
#         print("you are test associate")
#     else:
#         print("hired")
# s("engineering","hr")
# s("diploma","hr")



#fn with parameter
def reg(name,location,prefix="Mr/Mr"):
    if location == "salem":
        print(prefix,name,"has approved in",location)
    elif location == "chennai":
        print(prefix,name,"has waiting in",location)
    else:
        print("not approved")
reg("sri","salem")
