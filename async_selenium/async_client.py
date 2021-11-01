from aiohttp import ClientSession
from selenium.webdriver.remote.errorhandler import ErrorHandler, ErrorCode


class Command:

    async def _command(self, method, url, session: ClientSession, **kwargs):
        async with session.request(method, url) as resp:
            status_code = resp.status
            if 300 < status_code < 400:
                # 处理重定向
                return self._command('GET', resp.headers.get('location', ''), session)

            json_res = resp.json()

            if 399 < status_code < 500:
