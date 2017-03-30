# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:48:16
#   作者：kk
#-------------------------

from jieba import *

class jiebaTool(object):
    def __init__(self):
        pass
    #分词，全分词
    def cutContent(self,content):
        return jieba.cut(content,cut_all=True)

    #关键词提取，top-tags
    def analysisWithExtractTags(self,content,tags):
        return jieba.analyse.extract_tags(content,tags)

    def jieba_posseg(self,content):
        pass