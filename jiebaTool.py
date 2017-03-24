# -*- coding: utf-8 -*-
#-------------------------
#   版本：
#   日期：
#   作者：kk
#-------------------------

import jieba

class jiebaTool(object):
    def __init__(self):
        pass

    def cutContent(self,content):
        seg_list = jieba.cut(content,cut_all=True)
        return seg_list