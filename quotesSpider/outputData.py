# -*- coding: utf-8 -*-

import json


class OutputData(object):
    def outputTxt(self, datas):
        """
        将数据输出到文件
        :param data: 数据
        :return:
        """
        if datas is None:
            return
        # print(type(datas))
        # print(datas)
        with open('quotes.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(json.dumps(data, ensure_ascii=False) + '\n')
