# coding=utf-8
D = {}
D[1] = 'dd'
D['people'] = 108
print(D)
D2 = {'a': 1, 'b': 2, 'c': 3}
print(D2)
print(sorted(D2))
print(D2)
for key in D2.keys():
    print(D2[key])
x = 3
while x > 0:
    x -= 1
    print(sorted(D2)[x])
print'a' in D2, 'd' in D2
# 只在2.X版本有用
print D2.has_key('f')

T = (1, 'haha', 1, 1, 2)
print(T.count(1))
print(T.index('haha'))
