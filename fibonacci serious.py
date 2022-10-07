num=int(input("enter the limit:"))
a=0
b=1
s=0
for i in range(1,num+1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s