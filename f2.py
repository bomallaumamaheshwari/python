def add(a,b):
    return a+b;
def sub(a,b):
    return a-b;
def mul(a,b):
    return a*b;
def div(a,b):
    return float(a)/float(b);
print("Enter 2 nubers")
a=int(input())
b=int(input())
addition=add(a,b)
subtraction=sub(a,b)
multiplication=mul(a,b)
division=div(a,b)
print("Addition of 2 numbers",addition);
print("subtraction of 2 numbers",subtraction);
print("multiplication of 2 numbers",multiplication);
print("Division of 2 numbers",division);
