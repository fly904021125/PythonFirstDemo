# coding=utf-8
from decimal import Decimal
import fractions

d = Decimal('3.128')
d /= 3
print(d)
d = 3.128 / 3
print(d)
f = fractions.Fraction(2, 3)
print(f)
