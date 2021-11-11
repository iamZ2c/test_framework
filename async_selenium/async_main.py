from aiohttp import ClientSession
from async_webdriver import AsyncBrowser
import asyncio
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as Fserver
from config.settings import CHROME_DRIVER_PATH, CHROME_CAPS
from async_test import HomePage


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


def run():
    gec_server = Fserver("/Users/bytedance/Desktop/test_framework/driver/geckodrivers/geckodriver")
    gec_server.start()
    gec_server_url = gec_server.service_url
    server = Service(CHROME_DRIVER_PATH)
    server.start()
    server_url = server.service_url
    loop = asyncio.get_event_loop()
    utruef = asyncio.gather(main([HomePage], server_url, CHROME_CAPS),
                            main([HomePage], gec_server_url, {'capabilities': {}}))
    loop.run_until_complete(utruef)


if __name__ == '__main__':
    run()
