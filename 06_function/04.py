import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area,circumference

a,c = circle_stats(3)
print("area = ",round(a,2),"circumference = ",round(c,2))
# print("area = ",a,"circumference = ",c)