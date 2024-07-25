"""
Типизиация

Создал для SQL запросов, т.к некоторых типов данных которые есть
в SQL нету в Python, к примеру, BIGINTEGER.

Reques6e 2024
"""

from typing import NewType

BigInt = NewType('BigInt', int)
Int = NewType('Int', int)
Float = NewType('Float', float)
Bool = NewType('Bool', bool)
Str = NewType('Str', str)