str=input("Enter as a string:")
vowels=0
consonents=0

for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='u' or
       i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
       vowels=vowels+1;
    else:
        consonents=consonents+1;
print("the no of vowels",vowels)
print("The no of consonents",consonents)
