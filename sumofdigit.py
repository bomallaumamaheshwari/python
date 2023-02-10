n=int(input("enter a digit"))
sum=0
while n!=0:
    dig=int(n%10)
    sum+=dig
    n=n/10
print("sum of digit is ",sum)
