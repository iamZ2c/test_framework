from aiomysql import create_pool
from cx_Oracle import SessionPool
from reader.ini_reader import IniReader
from config import settings
from asyncio import get_event_loop,ensure_future


class DataBase:
    def __init__(self, database: str = 'mysql', autocommit: bool = True, *args, **kwargs):
        self._arg, self._kwargs = args, kwargs
        self._autocommit = autocommit

        if database.lower() == 'mysql':
            self._database = create_pool
            self._ini = IniReader(file_path=settings.DATA_BASE_FILE_PATH).data(database)
            self._loop = get_event_loop()
            self._mysql_pool = None
        if database.lower() == 'oracle':
            self._database = SessionPool
            self._ini = IniReader(file_path=settings.DATA_BASE_FILE_PATH).data(database)
            self._oracle_pool = None

    @property
    def oracle_pool(self):
        return self._database(*self._arg, **self._kwargs, self._ini)

    @property
    def mysql_pool(self):
        self._ini['autocommit'] = self._autocommit
        future = ensure_future(self._database(*self._arg, **self._kwargs, self._ini))
        self._loop.run_until_complete(future)
        return future.result()