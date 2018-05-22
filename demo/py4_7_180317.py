# coding=utf-8
# 有版本区别
L = []
print(type(L))
print(type(type(L)))

if type(L) == type([]):
    print('L is List')
else:
    print('L is not List')

if type(L) == list:
    print('L is List')
else:
    print('L is not List')

if isinstance(L, list):
    print('L is List')
else:
    print('L is not List')
