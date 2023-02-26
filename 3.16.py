from math import *


def gauss(x, m=0, s=10):
    n = 10
    length = ((m + 5 * s) - (m - 5 * s)) / n
    coordinates = []
    for i in range(0, n+1):
        x = m-5*s + i * length
        y = (1 / (sqrt(2 * pi) * s)) * exp(-1 / 2 * ((x - m) / s) ** 2)
        coordinates.append((x, y))
    return coordinates


for x, y in (gauss(x=1, m=0, s=10)):
    print(x, y)
