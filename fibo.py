n=int(input("enter a number"))
a=0
b=1
count=0
if n<=0:
    print("enter positive number")
elif n==1:
    print("fibo sequence of n is")
    print(a)
else:
    print("fibo sequence of n is ")
    while count<n:
        print(a)
        temp=a+b
        a=b
        b=temp
        count +=1
