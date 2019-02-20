# -*- coding: utf-8 -*-

import requests
import re


class Crawler(object):
    def get_page(self, url, **options):
        """
        获取页面的源码
        :param url:
        :return:
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36'
        }
        headers.update(options)
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print('抓取 {} 成功'.format(url))
                return response.text
            else:
                print('抓取 {} 代理失败'.format(url))
        except Exception as e:
            print('抓取 {} 代理失败,{}'.format(url, e))
            return None

    def run(self):
        """
        获取代理IP
        :return:
        """
        proxyes = []
        attrs = dir(Crawler)
        for item in attrs:
            if item.startswith('crawler_'):
                for proxy in eval('self.{}()'.format(item)):
                    proxyes.append(proxy)
        return proxyes

    def crawler_89ip(self, page_num=1):
        """
        爬取89ip代理
        :param page_num: 需要爬取的页码
        :return:
        """
        url = 'http://www.89ip.cn/index_{}.html'
        for i in range(1, page_num + 1):
            url = url.format(i)
            res = self.get_page(url)
            if res:
                pattern_ip = re.compile('<td>\s+(\d+\.\d+\.\d+\.\d+)\s+</td>')
                pattern_port = re.compile('<td>\s+(\d+)\s+</td>')
                proxy_ip = re.findall(pattern_ip, res)
                proxy_port = re.findall(pattern_port, res)
                for ip, port in zip(proxy_ip, proxy_port):
                    proxy = ip + ':' + port
                    yield proxy

    def crawler_xicidaili(self, page_num=1):
        """
        爬取西刺代理
        :param page_num:
        :return:
        """
        url = 'https://www.xicidaili.com/nt/{}'
        for i in range(1, page_num + 1):
            url = url.format(i)
            res = self.get_page(url)
            if res:
                pattern_ip = re.compile('<td>\s*(\d+\.\d+\.\d+\.\d+)\s*</td>')
                pattern_port = re.compile('<td>\s*(\d+)\s*</td>')
                proxy_ip = re.findall(pattern_ip, res)
                proxy_port = re.findall(pattern_port, res)
                for ip, port in zip(proxy_ip, proxy_port):
                    proxy = ip + ':' + port
                    yield proxy
