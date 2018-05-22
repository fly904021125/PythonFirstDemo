# coding=utf-8
import threename
from threename import a, b, c

print(threename.a, threename.b, threename.c)
print(a, b, c)
# 列出模块内的所有属性
print(dir(threename))
exec(open('threename.py').read())

