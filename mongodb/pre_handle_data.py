# -*- coding: utf-8 -*-
#-------------------------
#   版本：1.0
#   日期：2017年03月27日10:47:42
#   作者：kk
#-------------------------
from mongoConnector import *
from data_center import *
import codecs
import threading

class pre_handle_data(object):
    mongo = mongoConnector()
    dc = data_center()
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
        male_list = self.mongo.getMale

    def get_male_content(self):
        male_list = self.dc.get_males()
        male_list_count = len(male_list)
        threads = []
        for i in range(10):
            start = i*16000
            t = threading.Thread(target=self.content_dealer, args=(i,male_list[0+start:10000+start],))
            t.setDaemon(True)
            threads.append(t)
        for t in threads:
            t.start()

        for t in threads:
            t.join()


    '''
    处理信息的通用方法
    '''
    def content_dealer(self,sequence,list):
        # 构建所有男性的content
        male_temp_content = ""

        male_id_count = len(list)
        index = 0

        for person in list:
            index += 1
            print "%d  ----  now:  %d  of  %d" % (sequence,index, male_id_count)
            try:

                temp_content = ""
                temp_count = 0
                for tweet_bean in self.dc.get_tweets_by_id(person["ID"]):
                    temp_count += 1
                    print "current: " + tweet_bean["Content"]
                    temp_content += tweet_bean["Content"]
                    temp_content += "\n"
                # 少于10条不要
                if temp_count >= 10:
                    male_temp_content += temp_content
                    collection = self.mongo.getDB()["tweets_by_id"]
                    # 写入数据库
                    collection.insert({"content": temp_content}, {"sex": {1}})
                    # # 写入文件
                    # path = "/Users/Vincent/Desktop/_KKTest/Python/pro_data/%s.txt" % (person["ID"])
                    # print path
                    # with codecs.open(path, "w", "utf-8") as f:
                    #     f.writelines(temp_content)
                else:
                    self.mongo.db.male_id.remove({"ID": person["ID"]})
            except:
                print "there are error!"

            with codecs.open("/Users/Vincent/Desktop/_KKTest/Python/pro_data/male.txt", "w", "utf-8") as f:
                f.writelines(male_temp_content)






