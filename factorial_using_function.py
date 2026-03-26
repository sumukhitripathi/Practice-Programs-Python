#Factorial of a number using function
def calcFact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

n=int(input("Enter no for calculating factorial: "))
print("Factorial: ",calcFact(n))