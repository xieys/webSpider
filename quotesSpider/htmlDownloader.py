# -*- coding: utf-8 -*-

import requests


class HtmlDownloader(object):
    def downloader(self, url):
        """
        下载页面源码
        :param url: 页面URL
        :return:
        """
        if url:
            headers = {
                'user-agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit'
                              ' / 537.36(KHTML, likeGecko) Chrome / 70.0.3538.110Safari / 537.36'
            }
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                r.encoding = 'utf-8'
                return r.text
        return None
