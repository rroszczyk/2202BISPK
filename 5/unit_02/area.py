from math import pi

def circle_area(r):
    if type(r) not in [int, float]:
        raise TypeError("Promień okręgu musi być dodatnią liczbą rzeczywistą")
    if r < 0:
        raise ValueError("Promień okręgu nie może być wartością ujemną")
    return pi * (r**2)