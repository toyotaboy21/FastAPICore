import asyncio

from pydantic import BaseModel
from typing import Union

from fastcore.fastcore import FastCore
from fastcore.core.typedata import (
    BigInt, Int, Float, Bool, Str
)

db = FastCore(
    path='example.db'
)

class Item(BaseModel):
    name: Str
    price: Float
    is_admin: Int
    big_number: BigInt

async def main():
    await db.table_create(Item)

asyncio.run(main())
