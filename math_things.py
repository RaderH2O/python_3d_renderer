from math import sqrt
from typing import Tuple

def collide_lines(line1: Tuple[float, float, float], line2: Tuple[float, float, float]):
    m1, x1, y1 = line1
    m2, x2, y2 = line2
    b1 = (-x1) * m1 + y1
    b2 = (-x2) * m2 + y2
    y = (b1*m2 - b2 * m1) / (m2 - m1)
    x = (b1 - b2) / (m2 - m1)

    return (x, y)

def distance_of_pointline(point: Tuple[float, float], line: Tuple[float, float, float]):
    point_x, point_y = point
    m, x, y = line

    distance = abs(point_x * (-m) + point_y + (m * x) - y) / sqrt(1 + m**2)
    return distance

def sincos_from_tan(m):
    hypotenuse = 1 + m ** 2

    return (m/hypotenuse, 1/hypotenuse)