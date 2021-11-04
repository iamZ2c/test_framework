import requests
from selenium.webdriver.chrome.service import Service
from config.settings import CHROME_DRIVER_PATH, CHROME_CAPS,PROJECT_URL
import json

server = Service(CHROME_DRIVER_PATH)
server.start()
server_url = server.service_url + '/session'
session_url = server.service_url + '/session'
resp = requests.post(url=server_url, json=CHROME_CAPS)
sessionId = json.loads(resp.text)['value']['sessionId']

interface_url = server_url + f'/{sessionId}/url'

requests.post(url=interface_url, json={"url": PROJECT_URL})
