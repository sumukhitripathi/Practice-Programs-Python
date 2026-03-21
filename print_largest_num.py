#Tutorial 1
#wap to print largest of 3 no.s

a= int(input("Enter first no.: "))
b= int(input("Enter secondno.: "))
c= int(input("Enter third no.: "))
if (a>b and a>c):
    print(a, " is largest")
elif (b>a and b>c):
    print(b, " is largest")
else:
    print(c, " is largest")