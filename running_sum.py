#Tutorial 4
# Program to calculate the sum of positive numbers entered by the user until a negative number is entered

sum=0
while(True):
    n=int(input("Enter a positive no.: "))
    if (n<0):
        break
    sum+=n
print("the total sum is: ",sum)