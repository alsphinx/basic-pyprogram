num=int(input("enter the number"))
temp=num
sum=0
n=len(str(num))
while temp != 0:
    digit = temp % 10
    sum += pow(digit,n)
    temp //= 10

if sum == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")