# -*- coding: utf-8 -*-

from htmlDownloader import HtmlDownloader
from htmlParser import HtmlParser
from urlManager import UrlManager
from dataOutput import DataOutput


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.parser = HtmlParser()
        self.downloader = HtmlDownloader()
        self.output = DataOutput()

    def crawl(self, root_url):
        """
        程序主逻辑
        :param root_url: 入口 url
        :return:
        """
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 20:
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.downloader(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.output_txt(data)
                print(data)
                print("爬取了{}条链接".format(self.manager.old_url_size()))
            except Exception as e:
                print("爬取失败", e)


if __name__ == '__main__':
    spiderMan = SpiderMan()
    spiderMan.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")
