from time import sleep

from config.settings import PROJECT_URL
from util.decorector import add_async_log


async def get(async_driver, url):
    await async_driver.get(url)


class BasePage:
    async_driver = None

    async def get(self, url):
        await self.async_driver.get(url)


class HomePage(BasePage):
    @add_async_log
    async def test(self):
        await self.get(url=PROJECT_URL)
        await self.async_driver.send_keys('xpath', '//*[@id="su"]',text = "!23123")
        sleep(10)



