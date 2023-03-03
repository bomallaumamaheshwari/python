roll=int(input("enter student rollno"))
n=[1,2,3,4,5]
def stu(roll):
    if roll in n:
        print("student is present");
    else:
        print("Student is absent");
stu(roll)
