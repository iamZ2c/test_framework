# -*- coding:utf-8 -*-
from typing import List
import nest_asyncio
from aiomysql import create_pool, DictCursor
from cx_Oracle import SessionPool
from reader.ini_reader import IniReader
from config import settings
from asyncio import get_event_loop, ensure_future


class DataBase:
    def __init__(self, database: str = 'mysql', autocommit: bool = True, *args, **kwargs):
        self._arg, self._kwargs = args, kwargs
        self._autocommit = autocommit
        nest_asyncio.apply()
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
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), param)
                if rows:
                    res = await cur.fetchmany(rows)
                else:
                    res = await cur.fetchall()
        return res

    def select(self, sql: str, param: tuple, rows: [int, None] = None):
        self._loop.run_until_complete(future := ensure_future(self._select(sql, param, rows)))
        return future.result()

    async def _execute(self, sql: str, param: tuple):
        async with self.mysql_pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(sql.replace('?', '%s'), param)
                return cur.rowcount

    def execute(self, sql: str, param: tuple):
        self._loop.run_until_complete(future := ensure_future(self._execute(sql, param)))
        return future.result()


class OracleClient(DataBase):

    @classmethod
    def setUp(cls, *args, **kwargs):
        return cls(
            'oracle',
            *args,
            **kwargs
        )

    def select(self, sql: str, param: [list, None], row: [int, None], **kwargs):
        if param and kwargs:
            raise Exception(f'无法同时传入「{param}」「{kwargs}」两种参数！')
        with self._database().acquire() as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (param or kwargs))
                if row:
                    if row == 1:
                        res = cur.fetchone()
                    else:
                        res = cur.fetchmany(row)
                else:
                    res = cur.fetchall()
        return res

    def execute(self, sql: str, param: List[tuple], **kwargs):
        """

        :param sql:
        :param param: [('tom',1),('jan',2)]类似参数化。对数据进行批量修改

        :param kwargs:
        :return:
        """
        with self._database().acquire() as conn:
            with conn.cursor as cur:
                # 表描述第一个cur.description为列名
                columns = [col[0] for col in cur.description]
                # 定制cursor返回对象，加入字段名称，主要是修改cur.rowfactory属性
                cur.rowfactory = lambda *args: dict(zip(columns, *args))
                if param:
                    cur.executemany(sql, param)
                else:
                    cur.execute(sql, **kwargs)
                rowcount = cur.rowcount
            conn.commit()
        return rowcount


# 测试代码
a = MysqlClient.setUp()
print(a.select('SELECT * FROM isn_order', (),1))