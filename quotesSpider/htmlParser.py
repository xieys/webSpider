# -*- coding: utf-8 -*-

from lxml import etree
import urllib


class HtmlParser(object):
    def parser(self, page_url, html):
        """
        解析页面源码
        :param page_url: 页面URL
        :param html: 页面源码
        :return:
        """
        if html is None or page_url is None:
            return
        html = etree.HTML(html)
        # print(type(html))
        next_url = self._get_next_url(page_url, html)
        data = self._get_data(html)
        return next_url, data

    def _get_next_url(self, page_url, html):
        """
        获取新的URL
        :param page_url: 页面URL
        :param html: 页面源码
        :return:
        """
        next_url = html.xpath('//li[@class="next"]/a/@href')[0]
        new_url = urllib.parse.urljoin(page_url, next_url)
        print(new_url)
        return new_url

    def _get_data(self, html):
        """
        解析页面数据
        :param html: 页面源码
        :return:
        """
        datas = []
        items = html.xpath('//div[@class="quote"]')
        for item in items:
            text = item.xpath('.//span[@class="text"]/text()')[0].lstrip('“').rstrip('”')
            author = item.xpath('.//small[@class="author"]/text()')[0]
            tags = item.xpath('.//meta[@class="keywords"]/@content')[0]
            data = {
                "text": text,
                "author": author,
                "tags": tags
            }
            print(data)
            datas.append(data)
        return datas
