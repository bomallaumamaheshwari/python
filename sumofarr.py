arr = []
num = int(input("Enter the size of the array: "))
print("Enter array elements: ")
for i in range(num):
  numbers = int(input())
  arr.append(numbers)
print("Sum of array is ", sum(arr))
