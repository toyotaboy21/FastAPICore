"""
DataBase Exceptions

"""

class TableNotFound(Exception):
    pass


class DataBaseNotFound(Exception):
    pass


class ElementNotFound(Exception):
    pass


class DataBaseSTError(Exception):
    pass


class SQLStructure(Exception):
    pass


class DBOperationalError(Exception):
    pass


class DBError(Exception):
    pass


class DBKeyError(Exception):
    pass