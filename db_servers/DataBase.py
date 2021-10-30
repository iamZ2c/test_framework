from aiomysql import create_pool
from cx_Oracle import SessionPool
from reader.ini_reader import IniReader
from config import settings
from asyncio import get_event_loop, ensure_future


class DataBase:
    def __init__(self, database: str = 'mysql', autocommit: bool = True, *args, **kwargs):
        self._arg, self._kwargs = args, kwargs
        self._autocommit = autocommit

        if database.lower() == 'mysql':
            self._database = create_pool
            self._ini = IniReader(file_path=settings.DATA_BASE_FILE_PATH).data(database.upper())
            self._loop = get_event_loop()
            self._mysql_pool = None
        if database.lower() == 'oracle':
            self._database = SessionPool
            self._ini = IniReader(file_path=settings.DATA_BASE_FILE_PATH).data(database)
            self._oracle_pool = None

    @property
    def oracle_pool(self):
        return self._database(*self._arg, **self._kwargs, **self._ini)

    @property
    def mysql_pool(self):
        self._ini['autocommit'] = self._autocommit
        future = ensure_future(self._database(*self._arg, **self._kwargs, **self._ini))
        self._loop.run_until_complete(future)
        return future.result()


class MysqlClient(DataBase):

    @classmethod
    def setUp(cls, *args, **kwargs):
        return cls(
            *args,
            **kwargs
        )

    async def _select(self, sql: str, param: tuple, rows: [int, None]):
        async with self.mysql_pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.excute(sql.replace('?', '%s'), param)
                if rows:
                    res = await cur.fetchmany(rows)
                else:
                    res = await cur.fetchall()
        return res

    def select(self, *args, **kwargs):
        self._loop.run_until_complete(future := ensure_future(self._select(*args, **kwargs)))
        return future.result()