# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
import os


class Crawler(object):
    def get_html(self, url):
        if url:
            headers = {
                'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/72.0.3626.81Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                # response.text.encode('utf-8')
                print('获取链接{}源码成功'.format(url))
                return response.text
        print('获取链接{}失败'.format(url))
        return None

    def parse_cata(self, page_url, page_html):
        if page_html:
            cata = []
            html = etree.HTML(page_html)
            nav_li = html.xpath('//ul[@class="nav"]/li')
            # print(nav_li)
            for li in nav_li:
                item = {}
                item['url'] = li.xpath('./a[contains(@href,"=")]/@href')
                item['text'] = li.xpath('./a[contains(@href,"=")]/text()')
                if item['url']:
                    item['url'] = page_url + item['url'][0]
                    cata.append(item)
            return cata
        return None

    def parse_img_list(self, cata_list_url, img_list_html):
        if img_list_html:
            html = json.loads(img_list_html)
            if not html['end']:
                img_urls = []
                for item in html['list']:
                    list_id = item['id']
                    cata_list_url = cata_list_url.split('&')[0]
                    list_url = cata_list_url.replace('/zj?', '/zvj?') + '&id={}'.format(list_id)
                    print(list_url)
                    img_urls.append(list_url)
                return img_urls
            else:
                print('当前{}下的图片集url已经爬取完成。'.format(cata_list_url))
                return 'false'
        return None

    def parse_img_url(self, imgs_html):
        if imgs_html:
            html = json.loads(imgs_html)
            for item in html['list']:
                img_key = item['imgkey']
                img_url = item['qhimg_url']
                img_title = item['pic_title']
                yield {
                    'img_key': img_key,
                    'img_url': img_url,
                    'img_title': img_title
                }
        return None


def downloader(data):
    r = requests.get(data['img_url'])
    file_path = data['img_title']
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    file_path = os.path.join(file_path, data['img_key'])
    with open(file_path, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    a = Crawler()
    start_url = 'http://api.image.haosou.com'
    catas_html = a.get_html(start_url)
    catas = a.parse_cata(start_url, catas_html)
    for cata in catas:
        sn = 0
        while True:
            url = cata['url'].replace('/z?', '/zj?') + '&sn={}'.format(sn)
            img_list_html = a.get_html(url)
            img_list = a.parse_img_list(url, img_list_html)
            sn = sn + 30
            print(img_list)
            if img_list == 'false':
                break
            elif img_list is None:
                continue
            else:
                for img in img_list:
                    img_list_html_group = a.get_html(img)
                    for i in a.parse_img_url(img_list_html_group):
                        downloader(i)
