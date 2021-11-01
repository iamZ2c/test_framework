# -*- coding: utf-8 -*-
import asyncio
from aiohttp import ClientSession
import aiohttp
import re
import time

qcc_url = 'https://www.qcc.com/web/search?key=%E8%87%B4%E5%8A%9B%E8%BF%9C&p=1'

qcc_headers = {
    "Cookie": "QCCSESSID=fel8fq7u41inmn6fr5r45lc5o1; UM_distinctid=17a7546991b5d3-073a40bb1f0ff8-34647600-1fa400-17a7546991c9f8; zg_did=%7B%22did%22%3A%20%2217a75469a4a190-0a097bd24aaee1-34647600-1fa400-17a75469a4b27c%22%7D; _uab_collina=162546519948249240260285; CNZZDATA1254842228=816872870-1625461513-https%253A%252F%252Fwww.baidu.com%252F%7C1625553318; acw_tc=701cc88d16255576385353041e157134658ad6c2ac5d76a7e014708e1a; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201625557638906%2C%22updated%22%3A%201625557754209%2C%22info%22%3A%201625465199184%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E4%BC%81%E6%9F%A5%E6%9F%A5%E7%BD%91%E7%AB%99%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.google.com.hk%22%2C%22cuid%22%3A%20%2240e355d7ae9a3c07339ee9df370320ca%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%7D",
    "cache-control": "max-age=0",
    "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    "sec-ch-ua-mobile": "?0",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": "https://www.qcc.com/web/search?key=%E8%87%B4%E5%8A%9B%E8%BF%9C&p=3",
    "accept-language": "zh-CN,zh;q=0.9"
}


def make_page(url: str, num: int) -> list:
    """
    翻页方法
    :param num:
    :param url:
    :return:
    """
    return ["{}&p={}".format(url, i) for i in range(1, num + 1)]


async def _get_detail_link(url1):
    """"
    异步请求网页
    """
    async with ClientSession(connector=aiohttp.TCPConnector(limit=64, verify_ssl=False)) as session:
        async with session.get(url=url1, headers=qcc_headers) as response:
            return await response.text(encoding='utf-8')


def get_detail_link(url1):
    loop1 = asyncio.get_event_loop()
    loop1.run_until_complete(future := asyncio.ensure_future(_get_detail_link(url1)))
    return future.result()


def get_future(url2):
    return asyncio.ensure_future(get_detail_link(url2))


def get_link_list(html_text: str) -> list:
    """
    抓取qcc当前页面所需要的链接
    :return:
    """
    # 单页面链接数据抓取正则
    re_pa = re.compile('<a target="_blank" href="(.*?)"')

    detail_url_list = re.findall(re_pa, html_text)

    return detail_url_list


def crawl_data(str1):
    """
    详情页面所获取数据的方法
    :param url_list:
    :return:
    """
    data_list = []
    # 详细信息数据解析正则
    company_name_re_pa = re.compile('<h1>(.*?)</h1>')
    code = re.compile('用代码为(.*?)，')

    try:
        var = {"company_name": re.search(company_name_re_pa, str1).group(1),
               "code": re.search(code, str1).group(1)
               }
        data_list.append(var)
    except Exception:
        pass
    return data_list


if __name__ == '__main__':
    url_list1 = make_page(qcc_url, 20)
    start_time = time.time()
    tasks = [asyncio.ensure_future(get_detail_link(url)) for url in url_list1]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    link_list = []
    for i in tasks:
        link_list += get_link_list(i.result())
    tasks = [asyncio.ensure_future(get_detail_link(url)) for url in link_list]
    loop.run_until_complete(asyncio.wait(tasks))
    data_list = []
    for i in tasks:
        data_list += crawl_data(i.result())
    print(data_list)
    end_time = time.time()
    print(end_time - start_time)
    print(len(data_list))
