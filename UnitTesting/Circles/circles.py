from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError('The radius can not be negative')
    if type(r) not in [int, float]:
        raise TypeError('The radius must non-negative real numbere')
    return pi*(r**2)

#print(circle_area(1))