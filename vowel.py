str=input("enter the string")
vow="aeiou"
for i in str:
    for j in vow:
        if i==j:
            print(i)
            print(len(i))