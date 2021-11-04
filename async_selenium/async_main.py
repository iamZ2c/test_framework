from time import sleep

from aiohttp import ClientSession
from async_webdriver import AsyncBrowser
import asyncio
from selenium.webdriver.chrome.service import Service
from config.settings import CHROME_DRIVER_PATH, CHROME_CAPS
from async_test import HomePage
import requests


async def main(cls_list, url, caps):
    async with ClientSession() as session:
        driver = await AsyncBrowser.start(remote_server_driver=url, capabilities=caps, http_session=session)
        async with driver as _driver:
            for cls in cls_list:
                cls.async_driver = _driver
                instance = cls()
                _attr_list = dir(instance)
                for attr in _attr_list:
                    if 'test' in attr:
                        await eval(f'instance.{attr}()')


if __name__ == '__main__':
    server = Service(CHROME_DRIVER_PATH)
    server.start()
    server_url = server.service_url

    loop = asyncio.get_event_loop()

    loop.run_until_complete(future := asyncio.ensure_future(main([HomePage], server_url, CHROME_CAPS)))
