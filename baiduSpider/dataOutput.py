# -*- coding: utf-8 -*-

import json


class DataOutput(object):
    def output_txt(self, data):
        """
        將数据写入到文件
        :param data: 数据
        :return:
        """
        with open('baike.txt', 'a', encoding='utf-8') as f:
            f.write(json.dumps(data, ensure_ascii=False) + '\n')
