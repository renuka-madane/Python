#Calculate Area of the cone (area of cone = 0.33 * pi * r * r * h) (int)

# Reading radius
radius = float(input("Enter radius of cone: "))

# Reading height
height = float(input("Enter height of cone: "))

# Calculating surface area of cone
area = int(3.141592 * 0.33 * (radius*radius) * height)

# Displaying area
print("Surface area = ", area)



