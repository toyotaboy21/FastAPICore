import aiosqlite
import sqlite3


from pydantic import BaseModel
from typing import Union, Type

from fastcore.core.exceptions.db import DBOperationalError, DBError, DBKeyError
from fastcore.core.typedata import (
    BigInt, Int, Float, Bool, Str
)


type_mapping = {
    Str: 'TEXT',
    Int: 'INTEGER',
    Float: 'REAL',
    Bool: 'BOOLEAN',
    BigInt: 'BIGINTEGER'
}


class Db:
    def __init__(self, path: str, structure: Type) -> None:
        self.path = path

    async def table_create(self, model: Type[BaseModel]):
        """
        Создание таблицы

        **Пример использования:**

        ```python
        class Item(BaseModel):
            name: str
            price: float
            is_admin: int

        async def main():
            await db.table_create(Item)
        ```
        
        """

        table_name = model.__name__.lower() 

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

    async def element_create(self, table: Type[BaseModel], data: BaseModel) -> None:
        """
        Создание элемента в таблице

        Пример использования:
        ```py

        ```
        """

        table_name = table.__name__.lower()

        columns = [field for field in data.__fields__.keys()]
        values = [getattr(data, column) for column in columns]

        columns_str = ', '.join(columns)
        placeholders = ', '.join('?' * len(values))

        sql_query = f'INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders})'

        try:
            async with aiosqlite.connect(self.path) as db:
                await db.execute(sql_query, values)
                await db.commit()
        except sqlite3.OperationalError as e:
            raise DBOperationalError(f'В процессе работы операции базы данных произошла ошибка: {e}')
        except Exception as e:
            DBError(f'Неизвестная ошибка {e}')
        return True

    async def element_update(self, table: Type[BaseModel], data: BaseModel, key: str) -> None:
        table_name = table.__name__.lower()
        
        if not hasattr(data, key):
            raise DBKeyError(f"Идентификационное поле в объекте данных отсутствует.")

        key_value = getattr(data, key)
        update_fields = {field: getattr(data, field) for field in data.__fields__.keys() if getattr(data, field) is not None and field != key}
        update_columns = [f"{column} = ?" for column in update_fields.keys()]
        values = list(update_fields.values())
        values.append(key_value)

        update_str = ', '.join(update_columns)
        sql_query = f'UPDATE {table_name} SET {update_str} WHERE {key} = ?'

        try:
            async with aiosqlite.connect(self.path) as db:
                await db.execute(sql_query, values)
                await db.commit()
        except sqlite3.OperationalError as e:
            raise DBOperationalError(f'В процессе работы операции базы данных произошла ошибка: {e}')
        except Exception as e:
            raise DBError(f'Неизвестная ошибка: {e}')
        return True
    

    class User:
        def __init__(self, model: Type) -> None:
            self.model = model

        async def create() -> None:
            """ Создание пользователя"""
            ...

        async def edit() -> None:
            """ Изменение пользователя"""
            ...

        async def delete() -> None:
            """ Удаление пользователя"""
            ...