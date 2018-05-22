# coding=utf-8

# 有版本区别，3.+只支持第一种写法
oct_num = 0o777
oct_num = 0777

bit_num = 0b1001
bit_num = 0B1001
hex_num = 0xf12f1
hex_num = 0Xf12f1
num = 1000
print hex(num)
print oct(num)
print bin(num)
print int('1000', 10)
print int('0x3e8', 16)

# 复数
complex_num = 4 + 2j
complex_num = complex(4, 2)
print(complex_num)
