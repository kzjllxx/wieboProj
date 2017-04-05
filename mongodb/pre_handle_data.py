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
from jieba import *
import jieba.posseg as pseg

class pre_handle_data(object):
    mongo = mongoConnector()
    dc = data_center()
    def __init__(self):
        pass

    def separate_sex(self):
        male_list,female_list = [],[]
        # 获得男女的ID列表
        male_list, female_list = self.mongo.getMaleAndFemaleUserInfo()

        male_collection = self.mongo.getDB()["male"]
        female_collection = self.mongo.getDB()["female"]
        try:
            for male in male_list:
                print "male: "+male["_id"]
                male_collection.insert(male)
            for female in female_list:
                print "female: "+female["_id"]
                female_collection.insert(female)
        except:
            print "error!!!"

    def separeteContentBySex(self):
        male_list = self.mongo.getMale()


    def cut_male_name(self):
        print "cutting male_name"
        list = self.mongo.getMale()
        result_list = self.cut_person_name(list)
        for words in result_list:
            print "words 111"
            with codecs.open("C:\Users\chenyx\Desktop\weiboProData\male_name.txt", "a", "utf-8") as f:
                content = words.word + " " + words.flag + '\r\n'
                f.writelines(content)

    def cut_female_name(self):
        print "cutting female_name"
        list = self.mongo.getFemale()
        result_list = self.cut_person_name(list)
        for words in result_list:
            with codecs.open("C:\Users\chenyx\Desktop\weiboProData\_female_name.txt", "a", "utf-8") as f:
                content = words.word + " " + words.flag + '\r\n'
                f.writelines(content)

    def cut_person_name(self,list):
        name_content = ""
        try:
            for person in list:
                print person
                name_content += person["NickName"]
                name_content += " \r\n"
        except:
            print "no nickname"
        return pseg.cut(name_content)



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
        # data_list = []
        index = 0
        #获取collection
        collection = self.mongo.getDB()["tweets_by_id"]
        for person in list:
            index += 1
            print "%d  ----  now:  %d  of  %d" % (sequence,index, count)
            try:

                temp_content = ""
                temp_count = 0
                total = self.dc.get_tweets_by_id(person["_id"]).count()
                #少于10条不要
                if total < 10:
                    if sex_tag == 1:
                        self.mongo.db.male.remove({"_id": person["_id"]})
                        print "male---less than 10 -- skip!"
                    else:
                        self.mongo.db.female.remove({"_id": person["_id"]})
                        print "female--less than 10 -- skip!"
                else:
                    for tweet_bean in self.dc.get_tweets_by_id(person["_id"]):
                        temp_count += 1
                        temp_content += tweet_bean["Content"]
                        temp_content += "\n"
                    # 写入数据库
                    collection.insert({"content": temp_content,"sex": sex_tag,"ID":person["_id"]})
                    # data_list.append({"content": temp_content,"sex": sex_tag})
                    # print "%d -------  tatal:  %d"%(sequence,len(data_list))
                    content += temp_content

                    # # 写入文件
                    # path = "/Users/Vincent/Desktop/_KKTest/Python/pro_data/%s.txt" % (person["ID"])
                    # print path
                    # with codecs.open(path, "w", "utf-8") as f:
                    #     f.writelines(temp_content)


            except:
                print "there are error!:  "+ person["_id"]

        # collection.insert(data_list)

        if sex_tag == 1:
            with codecs.open("C:\Users\chenyx\Desktop\weiboProData\male.txt", "w", "utf-8") as f:
                f.writelines(content)
        else:
            with codecs.open("C:\Users\chenyx\Desktop\weiboProData\_female.txt", "w", "utf-8") as f:
                f.writelines(content)





