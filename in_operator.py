def checkPos(num):
    if num in lst:
        print("The number is present in the list at index ",lst.index(num))
    else:
        print("The number is not present in the list.")

lst=[10,20,30,40,50]
num=int(input("Enter a number to check: "))
checkPos(num)