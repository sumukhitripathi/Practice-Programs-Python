# Exception Handling

try:
    num1 = int(input("Enter dividend: "))
    num2 = int(input("Enter divisor: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Divisor shouldn't be zero")
except ValueError:
    print("Enter number only")

else:
    print("The answer is", result)

finally:
    print("Execution complete")