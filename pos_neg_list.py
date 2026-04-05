lst=[10,20,-30,40,-50]
posList=list()
negList=list()
for i in range(len(lst)):
    if lst[i] >= 0:
        posList.append(lst[i])
    else:
        negList.append(lst[i])
print("The original list is: ",lst)
print("The positive numbers in the list are: ",posList)
print("The negative numbers in the list are: ",negList)