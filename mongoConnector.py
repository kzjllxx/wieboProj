# -*- coding: utf-8 -*-
#-------------------------
#   版本：
#   日期：
#   作者：kk
#-------------------------

from pymongo import MongoClient
import sys

class mongoConnector(object):
    client = MongoClient("127.0.0.1", 27017)
    db = client["sina"]
    def __init__(self):
        pass


    def getMaleAndFemaleUserInfo(self):
        # 选择mongodb库

        collection = self.db.Information

        print collection.count()
        resultCollection = collection.find({"Gender": {"$in": ("男", "女")}})

        # 练个数组
        male_list, female_list = [], []
        # 对男女进行分组
        for bean in resultCollection:
            try:
                if bean["Gender"] == u'男':
                    male_list.append(bean)
                else:
                    female_list.append(bean)
            except:
                print "error!!!!"

        return male_list, female_list

    def getUserTweetsByID(self,userID):
        collection = self.db.Tweets
        tweets_list = collection.find({"ID":userID})
        return tweets_list