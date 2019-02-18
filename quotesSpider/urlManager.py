# -*- coding: utf-8 -*-


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def has_new_url(self):
        """
        判断是否有未爬取的url
        :return:
        """
        return self.new_urls_size() != 0

    def get_new_url(self):
        """
        返回新的URL
        :return:
        """
        url = self.new_urls.pop()
        self.old_urls.add(url)
        return url

    def add_new_url(self, url):
        """
        添加新的URL
        :param url: 新的URL
        :return:
        """
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def new_urls_size(self):
        """
        未爬取集合的大小
        :return:
        """
        return len(self.new_urls)

    def old_urls_size(self):
        """
        爬取过集合的大小
        :return:
        """
        return len(self.old_urls)
