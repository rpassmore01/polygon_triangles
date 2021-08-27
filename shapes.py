import math
from turtle import *


def polygon(n, radius):
    beta = 360 / n
    alpha = 90 - beta/2
    for i in range(n):
        forward(radius)
        left(180 - (alpha))
        forward((math.sin(math.radians(beta/2))*radius)*2)
        left(180 - (alpha))
        forward(radius)
        left(180)


polygon(12, 200)
done()
