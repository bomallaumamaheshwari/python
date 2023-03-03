def maximum(a, b, c):
 
    if (a >= b) and (a >= c):
        largest = a
 
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
         
    return largest
 
a = int(input('enter'))
b = int(input('enter'))
c = int(input('enter'))
print(maximum(a, b, c))
