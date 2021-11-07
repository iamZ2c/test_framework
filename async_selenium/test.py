from time import sleep

import requests
from selenium.webdriver.chrome.service import Service
from config.settings import CHROME_DRIVER_PATH, CHROME_CAPS, PROJECT_URL
import json

server = Service(CHROME_DRIVER_PATH)
server.start()
server_url = server.service_url + '/session'
session_url = server.service_url + '/session'
resp = requests.post(url=server_url, json=CHROME_CAPS)
sessionId = json.loads(resp.text)['value']['sessionId']

interface_url = server_url + f'/{sessionId}/url'

requests.post(url=interface_url, json={"url": PROJECT_URL})
print(f"{session_url}/{sessionId}/element")
res = requests.post(url=f"{session_url}/{sessionId}/element", json={
    'using': 'xpath',
    'value': '//*[@id="kw"]'
})
res = json.loads(res.text)
element = res["value"]
element_id = list(element.values())[0]
print(element_id)
res = requests.post(url=f"{session_url}/{sessionId}/element/{element_id}/value", json={
    "text": "zxxxx",
    "value":"123123"
})
print(res.text)

# from selenium.webdriver import Chrome
# d = Chrome(CHROME_DRIVER_PATH)
# d.get("https://www.baidu.com/")
# d.find_element('xpath','//*[@id="kw"]').send_keys("123123")