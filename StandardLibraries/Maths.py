# -*-coding:Latin-1 -*

import math
from fractions import Fraction
import random

print(math.pow(15, 2))
print(math.degrees(2))
print(math.ceil(2.3))
print(math.floor(5.9))
print(math.trunc(5.8))

half = Fraction(1, 2)
quarter = Fraction(1, 4)
print(half)
print(quarter)
print(float(half))
print(half+quarter)

print(Fraction.from_float(0.5))

print(random.randrange(1, 10, 2))
print(random.randint(1, 6))
char_list = ['a', 'b', 'c', 'd', 'e']
print(random.choice(char_list))
print(random.shuffle(char_list))
print(char_list)