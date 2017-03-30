# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日16:03:42
#   作者：kk
#-------------------------

from mongoConnector import *

class data_center(object):
    mongo = mongoConnector()
    def __init__(self):
        pass

    def get_males(self):
        result_list = []
        for male in self.mongo.getMale():
            result_list.append(male)
        return result_list

    def get_females(self):
        result_list = []
        for female in self.mongo.getFemale():
            result_list.append(female)
        return result_list

    def get_tweets_by_id(self,temp_id):
        return self.mongo.getUserTweetsByID(temp_id)