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

    def get_female_content(self):
        print "正在处理女性信息"
        female_list = self.dc.get_females()
        self.start_content_analysis_with_threads(0,female_list)


    def get_male_content(self):
        print "正在处理男性信息"
        male_list = self.dc.get_males()
        self.start_content_analysis_with_threads(1,male_list)

    def start_content_analysis_with_threads(self,sex_tag,list):

        count = len(list)
        step = count/10 +1
        #线程池
        threads = []
        for i in range(10):
            start = i*step
            t = threading.Thread(target=self.content_dealer, args=(i,sex_tag,list[start:step+start],))
            t.setDaemon(True)
            threads.append(t)
        #开启线程
        for t in threads:
            t.start()
        #阻塞主线程
        for t in threads:
            t.join()


    '''
    处理信息的通用方法
    '''
    def content_dealer(self,sequence,sex_tag,list):
        # 构建总content
        content = ""
        #当前的处理总数
        count = len(list)
        #数据数组
        data_list = []
        index = 0
        #获取collection
        collection = self.mongo.getDB()["tweets_by_id"]
        for person in list:
            index += 1
            print "%d  ----  now:  %d  of  %d" % (sequence,index, count)
            try:

                temp_content = ""
                temp_count = 0
                total = self.dc.get_tweets_by_id(person["ID"]).count()
                #少于10条不要
                if total < 10:
                    self.mongo.db.male_id.remove({"ID": person["ID"]})
                    print "less than 10 -- skip!"
                else:
                    for tweet_bean in self.dc.get_tweets_by_id(person["ID"]):
                        temp_count += 1
                        print "current: " + tweet_bean["Content"]
                        temp_content += tweet_bean["Content"]
                        temp_content += "\n"
                    print "ready to append"
                    # 写入数据库
                    # collection.insert({"content": temp_content}, {"sex": sex_tag})
                    data_list.append({"content": temp_content,"sex": sex_tag})
                    print "%d -------  tatal:  %d"%(sequence,len(data_list))
                    content += temp_content

                    # # 写入文件
                    # path = "/Users/Vincent/Desktop/_KKTest/Python/pro_data/%s.txt" % (person["ID"])
                    # print path
                    # with codecs.open(path, "w", "utf-8") as f:
                    #     f.writelines(temp_content)


            except:
                print "there are error!:  "+ person["ID"]

        collection.insert(data_list)

        with codecs.open("/Users/Vincent/Desktop/_KKTest/Python/pro_data/male.txt", "w", "utf-8") as f:
            f.writelines(content)






