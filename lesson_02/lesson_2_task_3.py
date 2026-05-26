import math


def square(side):
    area = side * side
    if type(side) != int:
        area = math.ceil(area)
    return area


print(square(4))
print(square(4.3))
