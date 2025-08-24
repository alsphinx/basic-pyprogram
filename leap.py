yr=int(input("enter the yr"))
if(yr%4==0 and yr%100!=0):
    print("u hv enterd a leapp yera")
elif (yr/400==0):
    print("u hv enterd a leapp yer")
else:
    print("not a leap yr ")