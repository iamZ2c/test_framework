from config.settings import PROJECT_URL


async def get(async_driver, url):
    await async_driver.get(url)


class BasePage:
    async_driver = None

    async def get(self, url):
        await self.async_driver.get(url)


class HomePage(BasePage):
    async def test(self):
        await self.get(PROJECT_URL)
        await self.async_driver.click('xpath', '//*[@id="frame_box"]/header/header/div/span/span[3]')
