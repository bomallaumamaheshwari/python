def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
num=5;
print("Factorial of",num,"is",
fact(num))


s="How Are You"
print(s.upper())


