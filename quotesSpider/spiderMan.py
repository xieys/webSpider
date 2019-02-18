# -*- coding: utf-8 -*-

from urlManager import UrlManager
from htmlDownloader import HtmlDownloader
from htmlParser import HtmlParser
from outputData import OutputData


class SpiderMan(object):
    def __init__(self):
        self.manger = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = OutputData()

    def crawl(self, root_url):
        """
        主程序
        :param root_url: 入口 URL
        :return:
        """
        self.manger.add_new_url(root_url)
        while self.manger.has_new_url() and self.manger.old_urls_size() < 5:
            new_url = self.manger.get_new_url()
            html = self.downloader.downloader(new_url)
            next_url, data = self.parser.parser(new_url, html)
            self.manger.add_new_url(next_url)
            self.output.outputTxt(data)
            # print(data)


if __name__ == '__main__':
    spiderMan = SpiderMan()
    spiderMan.crawl("http://quotes.toscrape.com/")
