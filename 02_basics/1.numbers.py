import math
math.floor(2.5)
math.floor(-2.5)
math.ceil(2.5)
math.trunc(2.5)
math.trunc(-2.5)

# octal value(8)
0o20
oct(64)

# hex value(16)
0x20
hex(64)

# binary value
0b20
bin(64)

int('64',8)

# --------------------------------

import random
random.randint(1,10)

l1=[1,2,3,4,5]
random.choice(l1)

random.shuffle(l1)

from decimal import Decimal
Decimal('0.1') + Decimal('0.1') + Decimal('0.1')