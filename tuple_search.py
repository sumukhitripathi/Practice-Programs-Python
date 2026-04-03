n=int(input("Enter no of students: "))
names=[]
for i in range(n):
    name=input("Enter name: ")
    names.append(name)
names_t=tuple(names)
target_name=input("Enter name to search: ")
if target_name in names_t:
    print(target_name,"found in the tuple.")
else:
    print(target_name,"not found in the tuple.")