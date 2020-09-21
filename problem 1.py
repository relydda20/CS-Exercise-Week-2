#This program converts an angle from degrees into radians
def conversion(degree):
    pi = 3.14
    return (degree * (pi / 180))

degree = 150
radian = conversion(degree)
print("The value in degrees is:", degree)
print("The Value in radians is:", radian)