n=int (input("Enter the number of students: "))
marks=list()
for i in range (n):
    marks.append(int(input("Enter the marks of student: ")))

avg=sum(marks)/n
print("The average marks of the students is: ",avg)