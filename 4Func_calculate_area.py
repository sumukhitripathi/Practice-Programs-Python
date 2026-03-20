def area_circle(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area

radius = float(input("Enter the radius of circle: "))
print("The area of circle is: ", area_circle(radius))