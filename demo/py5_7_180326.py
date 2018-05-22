# coding=utf-8
from fractions import Fraction

a = Fraction(1, 2)
print(a)
b = Fraction('1.2')
print(b)
print(0.1 + 0.1 + 0.1 - 0.3)
# 分数可保持精度计算
print(Fraction('0.1') + Fraction('0.1') + Fraction('0.1') - Fraction('0.3'))
# 浮点转换为分数元组
print(2.5.as_integer_ratio())
f = 2.5
print(Fraction(*f.as_integer_ratio()))
# 分数混合类型运算的精度问题
x = Fraction(1, 3)
print(2.5 + x)
print(x + x)
print(x + 1)
# 浮点转换为分数元组的精度问题
print(4.0/3)
print((4.0/3).as_integer_ratio())
a=Fraction(*(4.0/3).as_integer_ratio())
print(a)
# 限制分母<=10保证精度
print(a.limit_denominator(10))
