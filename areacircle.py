
def circle_Area(rad):
    
    return 3.14 * (rad ** 2)

rad = float(input('enter the radius of the circle: '))

print("area of the circle is %.6f " % circle_Area(rad))