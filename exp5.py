lst=list(map(int,input("Enter elements: ").split()))
print("Original list: ",lst)
def sorting_list(lst):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst
print("Sorted list: ",sorting_list(lst))