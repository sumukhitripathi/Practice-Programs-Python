lst=[10,20,30,40,50]
count = 0
num=int(input("Enter a number to check: "))
for i in range(len(lst)):
    if lst[i] == num:
        count += 1
print("The number occurs ",count," times in the list.")