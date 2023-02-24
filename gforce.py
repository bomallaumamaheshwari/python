m1=float(input("enter mass 1: "))
m2=float(input("enter mass 2: "));
r=float(input("enter the distance: "))
G=6.673*(10**-11);
f=(G*m1*m2)/r**2
print("gravitational force is",round(f,2),"N")
