a=int(input("enter the name"))
b=int(input("enter the name"))
c=int(input("enter the name"))
d=int(input("enter the name"))
if(a>b and a>c and a>d):
    print("a is lage")
elif(a<b and b>c and c>d):
    print("b is large")
elif(b<c and d<c):
    print("c is large")
else:
    print("d is lager")4
