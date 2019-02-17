# -*- coding: utf-8 -*-
import requests


class HtmlDownloader(object):

    def downloader(self, url):
        """
        获取链接网页源码
        :param url: 目标链接
        :return:
        """
        if url:
            headers = {
                'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) '
                              'Chrome / 72.0.3626.81Safari / 537.36',
            }
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                # 为了防止发生编码问题，先声明编码方式
                r.encoding = 'utf-8'
                # print(r.text)
                return r.text
        return None
