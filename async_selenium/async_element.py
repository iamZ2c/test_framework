from async_http_client import Command


class Element(Command):
    def __int__(self, element, url, session):
        """

        :param element:{element_name: element_id}
        :param url: http://remote_server_ip:port/session/session_id
        :param session:
        :return:
        """
        self.element_id = element.values()[0]
        self.url = url
        self.session = session
        self.api = f"{self.url}/element/{self.element_id}"
        self.session_id = self.url.split('/')[-1]

    async def _command(self, method, endpoint, **kwargs):
        return await super(Element, self)._command(method, self.url + endpoint, self.session, **kwargs)

    async def text(self):
        return await self._command('GET', '/text')

    async def send_keys(self, *keys):
        json = {
            'text': " ".join(*keys)
        }
        return await self._command('POST', '/value', json=json)

    async def click(self):
        json = {
            "id": self.element_id,
            "sessionId": self.session_id
        }
        return await self._command("POST", '/click', json=json)

    async def clear(self):
        json = {
            "id": self.element_id,
            "sessionId": self.session_id
        }
        return await self._command("POST", '/clear', json=json)

    # 完成元素类重写，疑问，如何获取session和sessionID