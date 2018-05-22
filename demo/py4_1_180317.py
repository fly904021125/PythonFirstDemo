# coding=utf-8
import re

s = 'human is so funny\n'
chinese_s = '人有时候真的很有意思吖'
print(s[2:3])
print(s[:4])
print(s[-3:])
print(s * 3 + ' haha')
print(s.find('is'))
print(s.find('的'))
print(s.split('s'))
print(chinese_s.replace('人', 'People'))
print(s.upper())
print(s.isalpha())
# 去除尾部空白字符
print(s.rstrip())
format_s = '%s is %s' % ('Lisa', 'a beauty')
print(format_s)
# 2.6 3.0以上才可使用
format_s = '{0} is {1}'.format('Lisa', 'beauty')
print(format_s)
print(len(s))
print(ord('\n'))
print(ord('a'))
print('hello\0\1girl')

tmatch = re.match('human[ \t].*biubiu', s)
print(tmatch)
tmatch = re.match('human[ \t](.*)', s)
print(tmatch.groups())
print(tmatch.groups(1))
