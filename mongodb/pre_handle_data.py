# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:47:42
#   作者：kk
#-------------------------
from mongoConnector import *
class pre_handle_data(object):
    mongo = mongoConnector()

    def __init__(self):
        pass

    def separate_sex(self):
        male_list,female_list = [],[]
        # 获得男女的ID列表
        male_list, female_list = self.mongo.getMaleAndFemaleUserInfo()

        male_collection = self.mongo.getDB()["male_id"]
        female_collection = self.mongo.getDB()["female_id"]
        try:
            for male in male_list:
                print "male: "+male["_id"]
                male_collection.insert({"ID":male["_id"]})
            for female in female_list:
                print "female: "+female["_id"]
                female_collection.insert({"ID":female["_id"]})
        except:
            print "error!!!"

    def separeteContentBySex(self):
        male_list = self.mongo.getMale()


