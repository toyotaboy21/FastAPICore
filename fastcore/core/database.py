import aiosqlite

from pydantic import BaseModel
from typing import Union, Type

from fastcore.core.typedata import (
    BigInt, Int, Float, Bool, Str
)

class Db:
    def __init__(self, path: str) -> None:
        self.path = path

    async def table_create(self, model: Type[BaseModel]):
        '''
        Создание таблицы

        **Пример использования:**
        ```py
        class Item(BaseModel):
            name: str
            price: float
            is_admin: int

        async def main():
        await db.table_create(Item)
        ```
        '''

        table_name = model.__name__.lower() 

        type_mapping = {
            Str: 'TEXT',
            Int: 'INTEGER',
            Float: 'REAL',
            Bool: 'BOOLEAN',
            BigInt: 'BIGINTEGER'
        }

        fields = []
        for name, field in model.__annotations__.items():
            field_type = type_mapping.get(field, 'TEXT')
            fields.append(f'{name} {field_type}')

        fields_def = ', '.join(fields)
        create_table_query = f'CREATE TABLE IF NOT EXISTS {table_name} ({fields_def});'

        async with aiosqlite.connect(self.path) as db:
            await db.execute(create_table_query)
            await db.commit()

            return True
        
    class User:
        def __init__(self) -> None:
            pass

        async def create() -> None:
            """ Создание пользователя"""
            ...

        async def edit() -> None:
            """ Изменение пользователя"""
            ...

        async def delete() -> None:
            """ Удаление пользователя"""
            ...