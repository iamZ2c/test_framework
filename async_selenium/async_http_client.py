from aiohttp import ClientSession
from icecream import icecream
from selenium.webdriver.remote.errorhandler import ErrorHandler, ErrorCode
from util.decorector import add_async_log


class Command:
    _error_handler = ErrorHandler()

    async def _command(self, method: str, url: str, session: ClientSession, **kwargs):
        print(url)
        async with session.request(method, url, **kwargs) as resp:
            status_code = resp.status
            if 300 < status_code < 400:
                # 处理重定向
                return self._command('GET', resp.headers.get('location', ''), session)
            json_res = await resp.json()
            if 399 < status_code < 500:
                # 返回的json对象必须要有status才能被ErrorHandler处理
                json_res['status'] = status_code
            if 199 < status_code < 400:
                json_res['status'] = ErrorCode.SUCCESS
            else:
                json_res['status'] = ErrorCode.UNKNOWN_ERROR
            print(json_res['value'])
            # 如果状态正确就直接返回结果,否则抛出错误和错误信息
            self._error_handler.check_response(json_res)
            return json_res['value']
