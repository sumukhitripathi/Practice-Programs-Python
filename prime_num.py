#Tutorial 3
#Check whether a number is prime or not

n=int(input("Enter a no.: "))
for i in range (2,int(n**0.5 +1)):
    if (n%i==0):
        print("Not a prime number")
        break
else:
    print("Prime no.")