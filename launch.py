# -*- coding: utf-8 -*-
#-------------------------
#   版本：
#   日期：
#   作者：kk
#-------------------------

from mongoConnector import *
from jiebaTool import  *
import jieba.analyse
#连接mongoDB
mongo = mongoConnector()

male_list,female_list = mongo.getMaleAndFemaleUserInfo()
temp_tweets_list = mongo.getUserTweetsByID(male_list[0]["_id"])

temp_content = ""
for temp_bean in temp_tweets_list:
    temp_content += temp_bean["Content"]

# seg_list = jiebaTool().cutContent(temp_content)
list = jieba.analyse.extract_tags(temp_content,50)
for bean in list:
    print bean


