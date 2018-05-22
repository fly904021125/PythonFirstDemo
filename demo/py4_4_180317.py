# coding=utf-8
# 有版本区别，3.X支持读取和写入二进制文件
f = open('file.txt', 'w')
f.write('hi\n')
f.writelines('girl')
f.write('my god')
f.close()
f = open('file.txt', 'rb')
s = f.read()
f.close()
print(s)
