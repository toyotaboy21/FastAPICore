# TypeData (Типизиация)

I created it for SQL queries, because some data types that exist in SQL are not available in Python.
in SQL are not available in Python, for example, BIGINTEGER.

```python
from fastcore.core.typedata import (
    BigInt, Int, Float, Bool, Str
)
```

For example, let's imagine that we have a `User` database structure:
```python
class User(BaseModel):
    name: Str
    price: Float
    is_admin: Int
    big_number: BigInt
```

Nothing much has changed, you can see the actual data types in the `fastcore.core.typedata` file