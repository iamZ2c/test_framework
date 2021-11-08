from time import sleep

from aiohttp import ClientSession
from icecream import ic

from async_selenium.async_element import AsyncElement
from async_selenium.async_http_client import Command
from selenium import webdriver


# webdriver.Chrome().get()


class AsyncBrowser(Command):

    @classmethod
    async def start(
            cls,
            remote_server_driver: str,
            capabilities: dict,
            http_session: ClientSession,
            reconnect_server_session: [str, None] = None):
        self = cls()
        self._http_session = http_session
        self._remote_server_driver = remote_server_driver
        self._desired_capabilities = capabilities
        if reconnect_server_session is None:
            # 获取sessionId
            async with self._http_session.post(f'{self._remote_server_driver}/session',
                                               json=self._desired_capabilities) as resp:
                res = await resp.json()
                self._browser_session_id = res['value'].get('sessionId', None) or res.get('sessionId', None)
        else:
            self._browser_session_id = reconnect_server_session
        self.url = f'{self._remote_server_driver}/session/{self._browser_session_id}'
        return self

    @property
    def _session_id(self):
        return getattr(self, '_browser_session_id')

    @property
    def _url(self):
        return getattr(self, 'url')

    @property
    def _session(self):
        return getattr(self, '_http_session')

    async def _command(self, method: str, endpoint: str, **kwargs):
        return await super(AsyncBrowser, self)._command(method, self._url + endpoint, self._session, **kwargs)

    async def get(self, url: str):
        body = {
            "url": url
        }
        return await self._command("POST", "/url", json=body)

    async def find_element(self, strategy: str, value: str, endpoint: str = '/element'):
        if strategy == 'id':
            strategy = 'css selector'
            value = "[id=%s]" % value
        elif strategy == 'name':
            strategy = 'css selector'
            value = "[name=%s]" % value
        elif strategy == 'class':
            strategy = '.%s' % value
        body = {
            'using': strategy,
            'value': value
        }
        # 返回一个json，从json里面获取元素
        element_info = await self._command('POST', endpoint, json=body)
        print(element_info)
        return AsyncElement(element_info, self._url, self._session)

    async def click(self, *location):
        element = await self.find_element(*location)
        return await element.click()

    async def send_keys(self, *location, text: str):
        element = await self.find_element(*location)
        return await element.send_keys(text)

    async def clear(self, *location):
        element = await self.find_element(*location)
        return await element.clear()

    async def text(self, *location):
        element = await self.find_element(*location)
        return await element.text

    async def get_title(self):
        return await self._command('GET', endpoint="/title")

    async def current_url(self):
        return await self._command('GET', endpoint="/url")

    async def screenshot(self):
        return await self._command('GET', endpoint="/screenshot")

    async def quit(self):
        return await self._command('DELETE', endpoint="")

    # 定义with用法
    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.quit()
