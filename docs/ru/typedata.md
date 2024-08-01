# TypeData (Типизиация)

Создал для SQL запросов, т.к некоторых типов данных которые есть
в SQL нету в Python, к примеру, BIGINTEGER.

```python
from fastcore.core.typedata import (
    BigInt, Int, Float, Bool, Str
)
```

К примеру, представим, что у нас есть структура базы данных `User`:
```python
class User(BaseModel):
    name: Str
    price: Float
    is_admin: Int
    big_number: BigInt
```

Особо ничего не изменилось, посмотреть актуальные типы данных можно посмотреть в файле `fastcore.core.typedata`