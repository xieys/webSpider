# -*- coding: utf-8 -*-
import urllib
from lxml import etree


class HtmlParser(object):
    def parser(self, page_url, html):
        """
        解析页面上的数据
        :param page_url: 下载页面的 url
        :param html: 下载页面源码
        :return:
        """
        if page_url is None or html is None:
            return
        html = etree.HTML(html)
        new_urls = self._get_new_url(page_url, html)
        data = self._get_data(page_url, html)
        return new_urls, data

    def _get_new_url(self, page_url, html):
        """
        获取页面为爬取的 url
        :param page_url: 下载页面的 url
        :param html: 下载页面源码
        :return:
        """
        new_urls = set()
        links = html.xpath('//a[contains(@href,"item")]/@href')
        for link in links:
            new_url = urllib.parse.urljoin(page_url, link)
            new_urls.add(new_url)
        return new_urls

    def _get_data(self, page_url, html):
        """
        获取页面中的数据
        :param page_url: 下载页面的url
        :param html: 下载页面的源码
        :return:
        """
        title = html.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()')[0]
        summary = "".join(html.xpath('//div[@class="lemma-summary"]//text()')).strip()
        data = {
            "url": page_url,
            "title": title,
            "summary": summary
        }
        return data
