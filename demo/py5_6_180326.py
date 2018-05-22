# coding=utf-8
# 浮点数精度问题
from decimal import Decimal
import decimal

print(0.1 + 0.1 + 0.1 - 0.3)
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
print(0.1 + 0.1 + 0.1 - 0.2)
print(0.1 + 0.1 - 0.2)
decimal.getcontext().prec = 4
print(Decimal('3.0') / Decimal('7'))
decimal.getcontext().prec = decimal.DefaultContext.prec
print(Decimal('3.0') / Decimal('7'))
# 临时精度
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(Decimal('3.0') / Decimal('7'))
print(Decimal('3.0') / Decimal('7'))
