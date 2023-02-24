'''1
def f1(name,rollno):
    print(name,rollno)
f1("uma","1254")
f1("amu","1200")'''

'''2
def f1(*args):
    for i in args:
        print(i)

f1(1,2,3)
f1(4,5)'''

'''3
def f1(a,b):
    add=a+b
    sub=a-b
    return add,sub

res=f1(30,20)
print(res)'''

'''4
def f1(name,rollno=1200):
    print("Name:" , name, "rollno:", rollno)

f1("uma",1254)
f1("amu")'''

'''5
def f1(a,b):
    square=a**2

    def f2(a,b):
        return a+b
    add=f2(a,b)
    return add+5

res=f1(10,20)
print(res)'''

'''6
def f1(n):
    if n :
        return n+f1(n-1)
    else:
        return 0

res=f1(10)
print(res)'''

'''7
def f1(name, rollno):
    print(name, rollno)
f1("uma", 1254)
    
res = f1
res("amu", 1200)'''

#8 print(list(range(4,30,2)))

x=[10,20,50,22,90,45]
print(max(x)) 







