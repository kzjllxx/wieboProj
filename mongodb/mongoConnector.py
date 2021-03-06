# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:47:52
#   作者：kk
#-------------------------

from pymongo import MongoClient

class mongoConnector(object):
    client = MongoClient("127.0.0.1", 27017)
    db = client["new_sina"]
    def __init__(self):
        pass


    def getMaleAndFemaleUserInfo(self):
        # 选择mongodb库

        collection = self.db.Information

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


    def getDB(self):
        return self.db

    def getClient(self):
        return self.client

    def getMale(self):
        collection = self.db.male
        list = collection.find()
        return list

    def getFemale(self):
        collection = self.db.female
        return collection.find()

    def get_male_with_slice(self,start,end):
        return self.db.male_id.find()