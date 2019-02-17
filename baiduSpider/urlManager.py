# -*- coding: utf-8 -*-


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        """
        判断是否有没有爬取过的链接
        :return: 
        """
        return self.new_url_size() != 0

    def get_new_url(self):
        """
        获取一个未爬取过的链接
        :return: 
        """
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    def add_new_url(self, url):
        """
        將新的链接添加到集合中
        :param url: 一个链接
        :return: 
        """
        if url is None:
            return
        if url not in self.old_urls and url not in self.new_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        """
        將新的链接集合添加到未爬取的集合中
        :param urls: 多个链接
        :return: 
        """
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        """
        获取没有爬取过的链接集合的大小
        :return: 
        """
        return len(self.new_urls)

    def old_url_size(self):
        """
        获取爬取过的链接集合的大小
        :return: 
        """
        return len(self.old_urls)
